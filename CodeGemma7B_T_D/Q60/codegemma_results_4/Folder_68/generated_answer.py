from math import sqrt

def all_left_right_truncatable_prime(num):
    """
    Let x be the integer at index 1. The function should return the list of all left-and-right-truncatable prime numbers less than or equal to x.
    """
    if not num:
        return []
    x = num[1]
    ltpn = []
    for digits in range(x + 1):
        number = int(''.join(map(str, digits)))
        if is_prime(number):
            if is_ltpn(number):
                ltpn.append(number)
    ltpn.sort(reverse=True)
    return ltpn

def is_prime(number):
    """
    The function is_prime(number) should check if the number is prime.
    """
    if number < 2:
        return False
    if number in [2, 3]:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    limit = int(sqrt(number)) + 1
    while i <= limit:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def is_ltpn(number):
    """
    The function is_ltpn(number) should check if the integer is left-and-right-truncatable prime.
    """
    if '0' in str(number):
        return False
    digits = list(str(number))
    for i in range(len(digits)):
        digits.pop(0)
        number = int(''.join(map(str, digits)))
        if not is_prime(number):
            return False
        digits.pop(-1)
        number = int(''.join(map(str, digits)))
        if not is_prime(number):
            return False
    return True