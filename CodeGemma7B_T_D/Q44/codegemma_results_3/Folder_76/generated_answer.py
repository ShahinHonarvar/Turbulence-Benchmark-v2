def composite_nums_between_indices(nums):
    """
    Write a function called 'composite_nums_between_indices' that takes one argument, a list of positive integers.
    The function should return the set of all composite numbers in the given list that are between index 639 to index 975, both inclusive.
    If no composite number exists in the specified range, the function should return an empty set.
    """
    composites = set()
    for idx, num in enumerate(nums):
        if 639 <= idx <= 975 and num > 1 and (not is_prime(num)):
            composites.add(num)
    return composites

def is_prime(num):
    """
    Helper function to check if a number is prime.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True