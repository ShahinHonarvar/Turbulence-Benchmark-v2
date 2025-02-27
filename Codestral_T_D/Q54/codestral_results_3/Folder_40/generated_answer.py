from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[10]
    right_trunc = []
    for num in range(2, x):
        if all((isprime(int(str(num)[:i])) for i in range(1, len(str(num)) + 1))):
            right_trunc.append(num)
    return sorted(right_trunc, reverse=True)