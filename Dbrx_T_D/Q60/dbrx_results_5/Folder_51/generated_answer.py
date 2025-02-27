from sympy import isprime

def is_left_right_truncatable_prime(n):
    if '0' in str(n) or not isprime(n):
        return False
    while n > 10:
        n = int(str(n)[1:]) if n < 100 else int(str(n)[:-1])
        if not isprime(n):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[54]
    result = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)