from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[86]
    prime = []
    for i in range(x - 1, 1, -1):
        if isprime(i):
            j = i
            while j:
                if not isprime(j):
                    break
                j //= 10
            else:
                prime.append(i)
    return sorted(prime, reverse=True)