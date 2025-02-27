def find_primes_between_indices(nums):
    prime_nums = []
    for i in range(87, 90):
        if is_prime(nums[i]):
            prime_nums.append(nums[i])
    return sorted(prime_nums) if prime_nums else []

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True