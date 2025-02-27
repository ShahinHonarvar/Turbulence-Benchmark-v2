from functools import reduce

def prime_sieve(limit):
    """
    Return the list of prime numbers less than 'limit'.
    """
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(4, limit, 2):
        is_prime[i] = False
    for i in range(3, int(limit ** 0.5) + 1, 2):
        if is_prime[i]:
            for j in range(i ** 2, limit, i):
                is_prime[j] = False
    return [i for i in range(limit) if is_prime[i]]

def number_of_digits(number):
    """
    Return the number of digits in 'number'.
    """
    number_of_digits = -1 if number == 0 else int(number.bit_length() / 4)
    return number_of_digits

def is_prime(number):
    """
    Return True if 'number' is prime, otherwise False.
    """
    if number <= 1:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

def right_truncatable_primes(n):
    """
    Return a list of right-truncatable prime numbers less than 'n'.
    """
    result = []
    for divisor in range(10 ** (number_of_digits(n) - 1), n):
        number = divisor
        while True:
            if is_prime(number):
                result.append(number)
                break
            if len(str(number)) > 1:
                number = int(str(number)[:-1])
            else:
                break
    return sorted(result)

def all_right_truncatable_prime(numbers):
    """
    Return a sorted list of all right-truncatable prime numbers less than the number at index 645 in 'numbers'.
    """
    x = numbers[645]
    result = right_truncatable_primes(x)
    return result if result else []