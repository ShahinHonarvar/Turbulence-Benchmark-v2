def all_right_truncatable_prime(x):
    """
  Write a function called 'all_right_truncatable_prime' that takes an argument which is a tuple of positive integers. Let x be the integer at index 35. The function should return the sorted list of all right-truncatable prime numbers less than x. The returned list should be sorted in descending order. If there is no such right-truncatable prime number, the function should return an empty list. A right-truncatable prime number is a prime number that remains prime when the last rightmost digit is successively removed.
  """
    if not isinstance(x, tuple) or not all((isinstance(i, int) and i > 0 for i in x)):
        raise TypeError('Input argument must be a tuple of positive integers.')
    x = x[34]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            str_i = str(i)
            for j in range(len(str_i) - 1):
                str_i = str_i[:-1]
                if not is_prime(int(str_i)):
                    break
            else:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True