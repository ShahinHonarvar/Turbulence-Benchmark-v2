def helper_prime_generator(x):
    """
    Generates all prime numbers less than or equal to x.
    """
    for n in range(2, 1 + x):
        is_prime = True
        for j in range(2, 1 + int(n ** 0.5)):
            if n % j == 0:
                is_prime = False
                break
        if is_prime:
            yield n

def helper_left_truncatable_prime(p):
    """
    Checks if p is a left-truncatable prime number.
    """
    if '0' in str(p):
        return False
    l = str(p)
    len_l = len(l)
    for n in range(1, len_l + 1):
        del l[0]
        if int(l) % 2 == 0 or int(l) % 3 == 0 or int(l) % 5 == 0 or (int(l) % 7 == 0):
            return False
        elif len(l) == 1:
            return True
        elif int(l) > 10:
            if int(l) % 3 == 0:
                continue
            for j in range(5, 2 + int(l ** 0.5), 6):
                if int(l) % j == 0 or int(l) % (j + 2) == 0:
                    return False

def helper_right_truncatable_prime(p):
    """
    Checks if p is a right-truncatable prime number.
    """
    if '0' in str(p):
        return False
    l = str(p)
    len_l = len(l)
    for n in range(1, len_l + 1):
        l = l[:-1]
        if int(l) % 2 == 0 or int(l) % 3 == 0 or int(l) % 5 == 0 or (int(l) % 7 == 0):
            return False
        elif len(l) == 1:
            return True
        elif int(l) > 10:
            if int(l) % 3 == 0:
                continue
            for j in range(5, 2 + int(l ** 0.5), 6):
                if int(l) % j == 0 or int(l) % (j + 2) == 0:
                    return False

def all_left_right_truncatable_prime(x):
    """
    Returns a list of all left-right truncatable prime numbers less than or equal to x.
    """
    left_right_truncatable_prime = []
    for p in helper_prime_generator(x):
        if helper_left_truncatable_prime(p) and helper_right_truncatable_prime(p):
            left_right_truncatable_prime.append(p)
    return sorted(left_right_truncatable_prime)