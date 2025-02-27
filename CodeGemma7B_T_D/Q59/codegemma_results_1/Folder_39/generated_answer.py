def all_left_truncatable_prime(x):
    """
    This function takes an argument which is a tuple of positive integers. Let x be the integer at index 30. The function should return the list of all left-truncatable prime numbers less than x. The return list should be sorted in descending order. A left-truncatable prime number is a prime number that contains no 0 and if the leading leftmost digit is successively removed, then all resulting numbers are prime.
    """
    if not isinstance(x, tuple):
        raise TypeError('Input must be a tuple.')
    if not all((isinstance(n, int) and n > 0 for n in x)):
        raise ValueError('Input tuple must contain only positive integers.')
    if len(x) != 31:
        raise ValueError('Input tuple must have a length of 31.')
    result = []
    for i in range(1, x[30]):
        if str(i) == '0':
            continue
        if is_prime(i):
            if is_left_truncatable_prime(i):
                result.append(i)
    result.sort(reverse=True)
    return result

def is_prime(n):
    """
    This function checks if a number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    """
    This function checks if a number is left-truncatable prime.
    """
    str_n = str(n)
    for i in range(1, len(str_n)):
        if str_n[i] == '0':
            return False
        new_n = int(str_n[i:])
        if not is_prime(new_n):
            return False
    return True