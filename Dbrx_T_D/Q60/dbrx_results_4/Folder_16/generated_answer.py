from sympy import isprime

def all_left_right_truncatable_prime(args):
    x = args[792]
    result = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)

def is_left_right_truncatable_prime(num):
    if '0' in str(num) or not isprime(num):
        return False
    while num > 10:
        num = int(str(num)[1:])
        if not isprime(num):
            return False
    while num > 9:
        num = int(str(num)[:-1])
        if not isprime(num):
            return False
    return True