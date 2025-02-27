from sympy import isprime

def all_right_truncatable_prime(x):

    def check_prime(n):
        return isprime(n) and all((isprime(n[i:]) for i in range(1, len(str(n)))))
    return sorted([x for x in range(2, x) if check_prime(x)], reverse=True)