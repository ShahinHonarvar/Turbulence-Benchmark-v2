from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[50]
    result = []
    for i in range(2, x):
        if isprime(i) and (not str(i).startswith('0')) and all((isprime(int(str(i)[:j])) for j in range(2, len(str(i))))):
            result.append(i)
    return sorted(result, reverse=True)