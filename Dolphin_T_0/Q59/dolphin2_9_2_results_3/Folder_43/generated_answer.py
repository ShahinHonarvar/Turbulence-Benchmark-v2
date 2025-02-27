from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[89]
    return sorted([i for i in range(x - 1, 0, -1) if isprime(i) and all((isprime(int(str(i)[n:])) for n in range(len(str(i)))))], reverse=False)