from sympy import isprime

def all_left_truncatable_prime(x):
    return sorted([p for p in range(2, x) if all((isprime(int(str(p)[:i])) for i in range(1, len(str(p)))))], reverse=True)