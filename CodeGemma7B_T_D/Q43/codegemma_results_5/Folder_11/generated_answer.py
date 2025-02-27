def find_primes_between_indices(nums):
    primes = []
    for i in range(55, 77):
        if is_prime(nums[i]):
            primes.append(nums[i])
    primes.sort()
    return primes or []

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True