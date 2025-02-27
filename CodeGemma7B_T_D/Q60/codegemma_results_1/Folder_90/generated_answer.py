from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[466]
    result = []
    for i in range(2, x + 1):
        if isprime(i) and (not '0' in str(i)) and is_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)

def is_truncatable_prime(n):
    str_n = str(n)
    if str_n[0] == '0' or str_n[-1] == '0':
        return False
    for i in range(len(str_n) - 1):
        if not isprime(int(str_n[i + 1:])):
            return False
    return True