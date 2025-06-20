def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(nums):
    primes = [nums[i] for i in range(76, 93) if is_prime(nums[i])]
    return sorted(primes)