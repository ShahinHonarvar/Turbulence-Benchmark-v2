def find_primes_between_indices(nums):
    prime_numbers = []
    for i in range(70, 72):
        if is_prime(nums[i]):
            prime_numbers.append(nums[i])
    return sorted(prime_numbers, reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True