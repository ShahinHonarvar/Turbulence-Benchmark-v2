def find_primes_between_indices(nums):
    prime_indices = []
    for i in range(1, 6):
        if is_prime(nums[i]):
            prime_indices.append(nums[i])
    prime_indices.sort()
    return prime_indices

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True