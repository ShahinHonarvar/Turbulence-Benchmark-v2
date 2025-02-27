def composite_nums_between_indices(nums):
    """
    Return set of all composite numbers in 'nums' between index 34 to 55 (inclusive).
    """
    composites = set()
    for i in range(34, 56):
        if not is_prime(nums[i]):
            composites.add(nums[i])
    return composites

def is_prime(n):
    """
    Return whether 'n' is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True