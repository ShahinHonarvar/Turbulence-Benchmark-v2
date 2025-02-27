import sympy

def is_left_right_truncatable_prime(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    length = len(str_n)
    for i in range(length):
        left_trunc = int(str_n[i:])
        right_trunc = int(str_n[:length - i])
        if not sympy.isprime(left_trunc) or not sympy.isprime(right_trunc):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[61]
    return sorted([n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)])