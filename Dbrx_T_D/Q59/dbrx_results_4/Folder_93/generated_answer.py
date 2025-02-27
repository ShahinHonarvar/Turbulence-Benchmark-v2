from sympy import isprime

def all_left_truncatable_prime(args):
    if not args or len(args) == 0:
        return []
    x = args[10] if len(args) > 10 else 100

    def is_left_truncatable_prime(n):
        if n < 10 and isprime(n):
            return True
        for i in range(1, len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True
    return sorted(list(filter(is_left_truncatable_prime, range(2, x))))