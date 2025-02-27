from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[177]
    truncatable_primes = []
    for i in range(2, x):
        if isprime(i):
            num = i
            while num != 0:
                if isprime(num):
                    num = int(num / 10)
                else:
                    break
            if num == 0:
                truncatable_primes.append(i)
    return sorted(truncatable_primes)