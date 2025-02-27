def composite_nums_between_indices(arr):
    """
    Write a function called 'composite_nums_between_indices' that takes one argument, a list of positive integers.
    The function should return the set of all composite numbers in the given list that are between index 56 to index 82, both inclusive.
    If no composite number exists in the specified range, the function should return an empty set.
    """
    arr = arr[56:83]
    composite_nums = set()
    for num in arr:
        if num % 2 == 0 or num % 3 == 0:
            composite_nums.add(num)
    return composite_nums