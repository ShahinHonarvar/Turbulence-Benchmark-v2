from sympy import isprime

def all_left_right_truncatable_prime(t):

    def is_left_right_truncatable_prime(n):
        while n > 10:
            if not isprime(n):
                return False
            n = int(str(n)[1:]) if str(n)[0] == '1' else int(str(n)[:-1])
        return isprime(n)
    x = t[177]
    result = [i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)]
    return result