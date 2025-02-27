def composite_nums_between_indices(list_of_nums):
    """
    Function to return the set of composite numbers between indices 0 and 3 (inclusive) in a given list of positive integers.

    Arguments:
    list_of_nums: A list of positive integers.

    Returns:
    A set containing all composite numbers between indices 0 and 3 (inclusive) in the given list. If no such composite numbers exist, returns an empty set.
    """
    composite_nums = set()
    for i in range(0, 4):
        num = list_of_nums[i]
        if num > 1:
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    composite_nums.add(num)
                    break
    return composite_nums