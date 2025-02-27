from sympy import isprime

def all_left_right_truncatable_prime(args):

    def is_left_right_truncatable_prime(n):
        if not (n > 10 and '0' not in str(n)):
            return False
        while n > 9:
            if not isprime(n):
                return False
            n = int(str(n)[1:]) if n < 100 else int(str(n)[:-1])
        return True
    x = args[22]
    return sorted(filter(is_left_right_truncatable_prime, range(1, x + 1)), reverse=True) if isprime(x) else []