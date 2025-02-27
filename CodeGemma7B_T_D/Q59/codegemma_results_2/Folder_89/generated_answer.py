from itertools import combinations_with_replacement

def prime_num_limited(n):
    """
    Return True if n is a prime number, False otherwise. It is only being used for numbers up to 100,000 (the maximum for the original program).
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(dec):
    """
    Return true if dec is a left-truncatable prime number for any of digits <= 9. False otherwise.
    """
    dec_str = str(dec)
    if '0' in dec_str:
        return False
    for k in range(1, len(dec_str)):
        num = int(dec_str[k:])
        if not prime_num_limited(num):
            return False
    return True

def generate_all_left_truncatable_prime(x):
    """
    Return the list of all left-truncatable prime numbers less than x. It is sorted in descending order.
    """
    data = []
    for dec in range(2, x):
        if is_left_truncatable(dec) and prime_num_limited(dec):
            data.append(dec)
    data.sort(reverse=True)
    return data