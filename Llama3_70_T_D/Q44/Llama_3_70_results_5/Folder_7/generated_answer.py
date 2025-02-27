def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def composite_nums_between_indices(nums):
    return {num for i, num in enumerate(nums) if 527 <= i <= 538 and (not is_prime(num))}