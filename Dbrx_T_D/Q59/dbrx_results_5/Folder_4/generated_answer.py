from sympy import isprime

def all_left_truncatable_prime(m):

    def is_left_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n = n // 10
        return True
    result = []
    for i in range(m[0], m[1]):
        if is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)