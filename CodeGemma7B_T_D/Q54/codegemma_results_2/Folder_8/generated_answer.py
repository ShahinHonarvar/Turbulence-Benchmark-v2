from sympy import isprime

def all_right_truncatable_prime(a):
    s = sorted([y for y in [x for x in list(a) if isprime(x)] if f'{y // 10 ** int(len(str(y)) - 1)}' in a], reverse=True)
    return s if s else []