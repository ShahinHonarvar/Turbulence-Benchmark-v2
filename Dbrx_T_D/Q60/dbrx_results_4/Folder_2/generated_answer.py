from sympy import isprime

def all_left_right_truncatable_prime(bounds):
    x = bounds[618]
    result = []
    for num in range(10, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)

def is_left_right_truncatable_prime(num):
    if num < 11 or '0' in str(num):
        return False
    while num > 10:
        if not isprime(num):
            return False
        num = int(str(num)[1:]) if num % 10 else int(str(num)[:-1])
    return True