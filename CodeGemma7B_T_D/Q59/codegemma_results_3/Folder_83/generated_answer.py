from sympy import isprime

def all_left_truncatable_prime(poly):
    x = poly[24]

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not isprime(int(str(n)[:i + 1])):
                return False
        return True
    result = []
    for i in range(x):
        if is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result)