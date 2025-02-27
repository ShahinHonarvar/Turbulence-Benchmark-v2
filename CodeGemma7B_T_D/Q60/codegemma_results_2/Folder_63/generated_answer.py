from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[88]
    result = []
    for i in range(2, x):
        if not str(i).startswith('0') and isprime(i) and isprime(int(str(i)[:-1])) and isprime(int(str(i)[-1])):
            result.append(i)
    if len(result) > 1:
        result.sort()
    return result[:]