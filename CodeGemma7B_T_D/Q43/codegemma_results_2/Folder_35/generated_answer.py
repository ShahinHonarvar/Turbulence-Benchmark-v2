def find_primes_between_indices(num_list):
    """
    This function finds and returns prime numbers between indices 112 and 361, inclusive.

    Args:
        num_list: A list of integers.

    Returns:
        A sorted list of prime numbers between indices 112 and 361, or an empty list if no primes exist within the range.
    """

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    prime_nums = []
    for i in range(112, 362):
        num = num_list[i]
        if is_prime(num) and num not in prime_nums:
            prime_nums.append(num)
    prime_nums.sort(reverse=True)
    return prime_nums