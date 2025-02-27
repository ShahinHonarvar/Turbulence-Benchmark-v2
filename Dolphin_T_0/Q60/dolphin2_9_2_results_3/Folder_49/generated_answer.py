def all_left_right_truncatable_prime(x):
    """
    This function takes one argument which is a tuple of positive integers.
    Let x be the integer at index 14.
    The function should return the list of all left-and-right-truncatable prime numbers less than or equal to x.
    The return list should be sorted in ascending order.
    If no left-and-right-truncatable prime number exists in the specified range, the function should return an empty list.
    """
    truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            if check_truncatable(num):
                truncatable_primes.append(num)
    return sorted(truncatable_primes)

def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_truncatable(num):
    num_str = str(num)
    for digit in num_str:
        if digit == '0':
            return False
    for i in range(len(num_str) - 1):
        if not is_prime(int(num_str[i + 1:])):
            return False
        if not is_prime(int(num_str[:i + 1])):
            return False
    return True