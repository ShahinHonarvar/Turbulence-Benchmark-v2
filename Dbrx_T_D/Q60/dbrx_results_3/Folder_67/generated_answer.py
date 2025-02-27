from sympy import isprime

def all_left_right_truncatable_prime(t):

    def is_left_truncatable_prime(n):
        if n < 10:
            return isprime(n)
        return isprime(n) and is_left_truncatable_prime(int(str(n)[1:]))

    def is_right_truncatable_prime(n):
        if n < 10:
            return isprime(n)
        return isprime(n) and is_right_truncatable_prime(int(str(n)[:-1]))
    x = t[71]
    result = []
    for i in range(2, x + 1):
        if is_left_truncatable_prime(i) and is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)