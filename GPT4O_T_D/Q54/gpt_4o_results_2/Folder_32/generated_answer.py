from sympy import isprime

def all_right_truncatable_prime(t):
    if len(t) <= 42:
        return []

    def is_right_truncatable_prime(n):
        if not isprime(n):
            return False
        n_str = str(n)
        for i in range(len(n_str) - 1, 0, -1):
            if not isprime(int(n_str[:i])):
                return False
        return True
    x = t[42]
    result = [n for n in range(2, x) if is_right_truncatable_prime(n)]
    return sorted(result)