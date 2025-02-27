from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[52]
    result = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)

def is_left_right_truncatable_prime(num):
    if '0' in str(num):
        return False
    while len(str(num)) > 1:
        num = int(str(num)[1:])
        if not isprime(num):
            return False
        num = int(str(num)[:-1])
        if not isprime(num):
            return False
    return isprime(num)