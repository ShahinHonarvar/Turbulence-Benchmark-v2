from sympy import composite, isprime

def all_right_truncatable_prime(some_tuple):
    x = some_tuple[79]
    return sorted([i for i in range(2, x) if all((isprime(int(str(i)[:-j])) for j in range(1, len(str(i)))))], reverse=True)