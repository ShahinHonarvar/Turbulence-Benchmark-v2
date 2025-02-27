def find_primes_between_indices(nums):
    primes = []
    for i in range(45, 81):
        if is_prime(nums[i]):
            primes.append(nums[i])
    return sorted(primes, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True