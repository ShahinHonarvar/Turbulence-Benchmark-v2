from sympy import isprime

def all_left_truncatable_prime(args):
    x = args[3]
    result = []
    for num in range(1, x):
        if is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)

def is_left_truncatable_prime(num):
    if num < 10:
        return isprime(num)
    else:
        return is_left_truncatable_prime(num // 10) and isprime(num)