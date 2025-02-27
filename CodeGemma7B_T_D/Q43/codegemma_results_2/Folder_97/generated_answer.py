def find_primes_between_indices(nums):
    primes = []
    for i in range(295, 456):
        if is_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True