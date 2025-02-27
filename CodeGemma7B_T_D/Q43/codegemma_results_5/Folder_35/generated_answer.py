def find_primes_between_indices(nums):
    primes = []
    for i in range(112, 362):
        if is_prime(nums[i]):
            primes.append(nums[i])
    return sorted(primes, reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True