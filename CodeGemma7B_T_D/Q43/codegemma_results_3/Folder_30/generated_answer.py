def find_primes_between_indices(nums):
    primes = []
    for i in range(61, 81):
        if is_prime(nums[i]):
            primes.append(nums[i])
    primes.sort(reverse=True)
    return primes or []

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True