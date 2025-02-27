def find_primes_between_indices(nums):
    Primes = []
    for x in range(23, 60):
        if is_prime(nums[x]):
            Primes.append(nums[x])
    Primes.sort(reverse=True)
    return Primes

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True