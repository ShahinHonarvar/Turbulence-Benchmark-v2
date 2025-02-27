def composite_nums_between_indices(nums):
    composites_between = {num for num in nums[42:69] if not is_prime(num)}
    return composites_between if composites_between else set()

def is_prime(num):
    """Determines if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True