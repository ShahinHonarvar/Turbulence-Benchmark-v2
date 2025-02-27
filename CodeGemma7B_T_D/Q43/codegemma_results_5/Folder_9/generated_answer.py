def find_primes_between_indices(nums):
    """
    This function takes one argument, a list of integers,
    and returns the sorted list of all prime numbers from index 16 to index 71, both inclusive.
    The returned list should be in ascending order.
    If no prime number exists in the specified range, the function should return an empty list.
    """
    primes = []
    for i in range(16, 72):
        if is_prime(i):
            primes.append(i)
    return sorted(primes)

def is_prime(n):
    """
    This function checks if a number is prime.
    A number is prime if it is greater than 1 and has only two factors: 1 and itself.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True