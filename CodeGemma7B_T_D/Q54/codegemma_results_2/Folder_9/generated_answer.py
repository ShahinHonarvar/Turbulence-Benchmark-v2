from sympy import isprime

def all_right_truncatable_prime(n):
    ans = [y for y in range(2, int(n[29])) if isprime(y) and all((isprime(int(str(y)[:-i])) for i in range(1, len(str(y)))))]
    return sorted(ans, reverse=True)