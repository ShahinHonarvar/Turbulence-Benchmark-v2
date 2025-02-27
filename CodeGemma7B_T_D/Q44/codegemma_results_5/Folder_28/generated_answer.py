def composite_nums_between_indices(nums):
    return {n for i, n in enumerate(nums) if 22 <= i <= 88 and (not is_prime(n))}

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True