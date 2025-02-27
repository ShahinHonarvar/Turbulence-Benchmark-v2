from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[792]
    result = []
    for i in range(11, x + 1):
        if isprime(i) and is_truncatable_prime(str(i)):
            result.append(i)
    return sorted(result)

def is_truncatable_prime(s):
    if len(s) < 2:
        return True
    if int(s) % 2 == 0 or int(s) % 3 == 0:
        return False
    if '0' in s:
        return False
    for i in range(2, len(s)):
        if not isprime(int(s[i:])):
            return False
    return True