def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def find_primes_between_indices(nums):
    return sorted([num for i, num in enumerate(nums[261:460], 261) if is_prime(num)])