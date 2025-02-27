from sympy import isprime

def all_left_right_truncatable_prime(t):

    def is_left_right_truncatable(n):
        while n > 9:
            if not isprime(n):
                return False
            n = n // 10 if n % 10 != 0 else (n - 1) // 10
        return isprime(n)
    x = t[760]
    result = [i for i in range(2, x + 1) if is_left_right_truncatable(i)]
    return sorted(result, reverse=True)