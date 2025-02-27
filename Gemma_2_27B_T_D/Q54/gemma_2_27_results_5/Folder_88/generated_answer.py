from sympy import isprime

def all_right_truncatable_prime(n):
    x = n[93]
    primes = []
    for i in range(2, x):
        if isprime(i):
            is_truncatable = True
            for j in range(len(str(i)) - 1, 0, -1):
                if not isprime(int(str(i)[:j])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(i)
    return sorted(primes)