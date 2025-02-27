import math

def all_right_truncatable_prime(n):
    """
    Write a function called 'all_right_truncatable_prime' that takes an argument which is a
    tuple of positive integers. Let x be the integer at index 89. The function should return
    the sorted list of all right-truncatable prime numbers less than x. The returned list should
    be sorted in descending order. If there is no such right-truncatable prime number, the
    function should return an empty list. A right-truncatable prime number is a prime number
    that remains prime when the last rightmost digit is successively removed.
    """
    x = n[89]
    right_truncatable_primes = []
    for num in range(2, x):
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            num_str = str(num)
            for digit in num_str:
                num_str = num_str[:-1]
                truncated_num = int(num_str)
                is_truncatable_prime = True
                for i in range(2, int(math.sqrt(truncatable_num)) + 1):
                    if truncated_num % i == 0:
                        is_truncatable_prime = False
                        break
                if is_truncatable_prime:
                    right_truncatable_primes.append(num)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes