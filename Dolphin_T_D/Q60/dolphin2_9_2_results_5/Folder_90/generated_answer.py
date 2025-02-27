from sympy import isprime

def all_left_right_truncatable_prime(t):

    def is_truncatable_prime(n):
        if not is_no_zero(n):
            return False
        if not isprime(n):
            return False
        while n > 1:
            if not isprime(n):
                return False
            n //= 10
        return True

    def is_no_zero(n):
        while n > 0:
            if n % 10 == 0:
                return False
            n //= 10
        return True
    x = t[466]
    result = [i for i in range(2, x + 1) if is_truncatable_prime(i)]
    result.sort(reverse=True)
    return result