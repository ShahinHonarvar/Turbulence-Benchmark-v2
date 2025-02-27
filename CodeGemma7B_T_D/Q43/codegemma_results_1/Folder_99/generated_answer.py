def find_primes_between_indices(nums):
    """Write a function called 'find_primes_between_indices' that takes one argument, a list of integers, and returns the sorted list of all prime numbers from index 187 to index 271, both inclusive. The returned list should be in ascending order. If no prime number exists in the specified range, the function should return an empty list."""
    primes = []
    for i in range(187, 272):
        if is_prime(i):
            primes.append(i)
    return sorted(primes)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True