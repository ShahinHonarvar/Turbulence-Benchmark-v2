def composite_nums_between_indices(nums):
    """
    Write a function called 'composite_nums_between_indices' that takes one argument, a list of positive integers.
    The function should return the set of all composite numbers in the given list that are between index 2 to index 2, both inclusive.
    If no composite number exists in the specified range, the function should return an empty set.
    """
    composite_nums = set()
    for i in range(2, 2 + 1):
        if not (num % 2 == 0 or num % 3 == 0):
            composite_nums.add(num)
    return composite_nums