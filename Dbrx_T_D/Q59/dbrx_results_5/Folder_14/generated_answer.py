from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[78]
    primes = []
    for i in range(1, 10):
        prime = i
        while prime < x:
            if isprime(prime):
                found = True
                for j in range(len(str(prime)) - 1):
                    prime //= 10
                    if not isprime(prime):
                        found = False
                        break
                if found:
                    primes.append(prime)
            prime *= 10
            prime += i
    return sorted(primes, reverse=True)