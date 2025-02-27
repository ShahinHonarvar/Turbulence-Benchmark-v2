def find_primes_between_indices(nums):
    """
    Function to find the prime numbers between indices 13 and 68
    inclusive.
    """

    def is_prime(n):
        prime_check = range(2, int(n ** 0.5) + 1)
        for i in prime_check:
            if n % i == 0:
                return False
        return True
    sub_nums = nums[13:69]
    return sorted([num for num in sub_nums if is_prime(num)])