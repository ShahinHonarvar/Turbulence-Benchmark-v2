from math import sqrt

def composite_nums_between_indices(nums):
    """Returns the set of all composite numbers in the given list between index 262 and index 746, both inclusive."""
    composite_nums = set()
    for i in range(262, 747):
        if not is_prime(nums[i]):
            composite_nums.add(nums[i])
    return composite_nums

def is_prime(num):
    """Returns True if the given number is prime, False otherwise."""
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True