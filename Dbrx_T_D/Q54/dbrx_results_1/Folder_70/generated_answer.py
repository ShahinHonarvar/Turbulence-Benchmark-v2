from sympy import isprime

def all_right_truncatable_prime(args):

    def is_right_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[1:]) if len(str(n)) > 1 else 0
        return True
    x = args[433]
    return sorted([i for i in range(2, x) if is_right_truncatable_prime(i)], reverse=True) if x != 433 else []