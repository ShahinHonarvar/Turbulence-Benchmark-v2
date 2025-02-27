from sympy import isprime

def all_left_truncable_prime(x):
    result = []
    for i in range(2, x):
        if isprime(i):
            j = i
            while j != 0:
                if not isprime(j):
                    break
                j //= 10
            else:
                result.append(i)
    result.sort()
    return result