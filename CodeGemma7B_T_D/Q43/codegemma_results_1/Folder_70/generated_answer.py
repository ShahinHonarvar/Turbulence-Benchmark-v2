from index 131 to index 815, both inclusive. The returned list should be in descending order.

def find_primes_between_indices(nums):
    """
    This function takes a list of integers as an argument and returns a sorted list of all prime numbers
    If no prime number exists in the specified range, the function should return an empty list.

    Args:
        nums: A list of integers.

    Returns:
        A sorted list of prime numbers from index 131 to index 815, both inclusive. If no prime
        number exists in the specified range, the function should return an empty list.
    """

    def is_prime(num):
        """
        This function takes an integer as an argument and returns True if it is prime, False otherwise.

        Args:
            num: An integer.

        Returns:
            True if num is prime, False otherwise.
        """
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    primes = []
    for i in range(131, 816):
        if is_prime(i):
            primes.append(i)
    primes.sort(reverse=True)
    return primes