from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[37]
    result = []

    def is_trunc_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n = n // 10 if n != 1 else 0
        return True
    for i in range(2, x + 1):
        if is_trunc_prime(i) and isprime(i):
            result.append(i)
    return sorted(list(set(result)), reverse=True)