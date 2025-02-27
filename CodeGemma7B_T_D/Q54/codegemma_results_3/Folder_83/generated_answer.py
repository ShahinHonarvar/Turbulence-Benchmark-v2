from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[24]
    result = []
    for i in range(11, x):
        if isprime(i) and all((isprime(int(f'{i}{digit}')) for digit in str(i)[:-1])):
            result.append(i)
    return sorted(result)