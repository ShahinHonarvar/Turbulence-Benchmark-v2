def find_primes_between_indices(nums):
    primes = [nums[i] for i in range(11, 12)]
    return [i for i in primes if is_prime(i)]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True