from sympy import isprime

def all_right_truncatable_prime(range_tuple):
    x = range_tuple[79]
    result = []
    for num in range(1, x):
        if is_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)

def is_right_truncatable_prime(num):
    if not isprime(num):
        return False
    while num > 10:
        num = int(str(num)[:-1])
        if not isprime(num):
            return False
    return True