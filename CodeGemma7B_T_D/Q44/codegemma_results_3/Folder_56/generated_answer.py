def composite_nums_between_indices(list_of_nums):
    """
    This function takes one argument, a list of positive integers.
    The function should return the set of all composite numbers in the given list that are between index 0 to index 0, both inclusive.
    If no composite number exists in the specified range, the function should return an empty set.
    """
    composite_nums = set()
    for num in list_of_nums:
        if num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            composite_nums.add(num)
    return composite_nums