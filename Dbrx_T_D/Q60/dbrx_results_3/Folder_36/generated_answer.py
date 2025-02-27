from sympy import isprime

def truncate_left_right(n):
    while n > 10:
        n /= 10
        if not isprime(int(n)):
            return False
    return True

def all_left_right_truncatable_prime(tpl):
    x = tpl[992]
    result = []
    for num in range(2, x + 1):
        if isprime(num) and truncate_left_right(num):
            result.append(num)
    return sorted(result)