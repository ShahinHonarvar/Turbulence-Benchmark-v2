def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(nums):
    primes = [num for i, num in enumerate(nums) if 20 <= i <= 25 and is_prime(num)]
    return sorted(primes, reverse=True)