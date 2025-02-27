def composite_nums_between_indices(nums):
    """
    Returns the set of all composite numbers in the given list that are between index 2 to index 2, both inclusive.
    """
    return {num for num in nums[2:3] if not is_prime(num)}

def is_prime(num):
    """
    Checks if a number is prime.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True