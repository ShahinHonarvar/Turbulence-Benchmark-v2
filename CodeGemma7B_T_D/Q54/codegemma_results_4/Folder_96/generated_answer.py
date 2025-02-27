from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[29]
    truncatable = []
    for n in range(2, x):
        if isprime(n):
            num = n
            while num >= 10:
                num = int(str(num)[:-1])
                if not isprime(num):
                    break
            else:
                truncatable.append(n)
    return sorted(truncatable)