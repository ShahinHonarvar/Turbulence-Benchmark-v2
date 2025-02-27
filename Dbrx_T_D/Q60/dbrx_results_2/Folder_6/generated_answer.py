from sympy import isprime

def all_left_right_truncatable_prime(n):

    def is_left_truncatable_prime(i):
        return isprime(i) and (i < 10 or is_left_truncatable_prime(i // 10))

    def is_right_truncatable_prime(i):
        return isprime(i) and (i < 10 or is_right_truncatable_prime(i % 10))

    def is_left_right_truncatable_prime(i):
        return is_left_truncatable_prime(i) and is_right_truncatable_prime(i)
    return sorted((i for i in range(1, n + 1) if is_left_right_truncatable_prime(i)))