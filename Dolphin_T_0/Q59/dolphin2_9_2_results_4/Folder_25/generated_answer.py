def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(s):
    n = int(s)
    if str(n)[0] != '0' and is_prime(n):
        return is_truncatable_prime(str(n)[1:]) if str(n)[1:] != '' else True
    return False

def all_left_truncatable_prime(x):
    result = []
    for i in range(2, x):
        if is_truncatable_prime(str(i)):
            result.append(i)
    result.sort()
    return result