def all_left_truncatable_prime(x):
    return sorted(list(filter(left_truncatable_prime, range(2, x + 1))), reverse=True)

def left_truncatable_prime(n):
    if not is_prime(n):
        return False
    if not is_digit_prime(str(n)[0]):
        return False
    return all((str(n)[i] != '0' for i in range(1, len(str(n)) + 1)))

def is_prime(n):
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, 1 + int(n ** 0.5), 6):
        if n % i == 0:
            return False
    return True

def is_digit_prime(d):
    if d in '05':
        return False
    for i in range(5, len(d) + 1):
        if d[i - 1] not in '2357':
            return False
    return True