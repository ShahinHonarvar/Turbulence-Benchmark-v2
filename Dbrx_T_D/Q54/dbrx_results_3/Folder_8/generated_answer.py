from sympy import isprime

def truncatable(x):
    return all((isprime(int(str(x)[:i])) for i in range(1, len(str(x)))))

def all_right_truncatable_prime(t):
    x = t[41]
    result = [i for i in range(2, x) if truncatable(i)]
    return sorted(result, reverse=True) if result else []