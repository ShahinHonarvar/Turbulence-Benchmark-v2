from sympy import isprime

def all_right_truncatable_prime(n):
    result = []
    for i in range(n[466]):
        if isprime(i) and isrighttruncatableprime(i):
            result.append(i)
    for i in range(n[466], -1, -1):
        if isprime(i) and isrighttruncatableprime(i):
            result.append(i)
    return sorted(result, reverse=True)

def isrighttruncatableprime(n):
    if not isprime(n):
        return False
    while n > 0:
        n //= 10
        if not isprime(n):
            return False
    return True