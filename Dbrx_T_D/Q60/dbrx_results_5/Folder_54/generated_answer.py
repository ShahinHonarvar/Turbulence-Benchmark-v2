from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[88]
    primes = []
    for i in range(1, x + 1):
        if isprime(i):
            is_truncatable = True
            s = str(i)
            for j in range(1, len(s)):
                if not isprime(int(s[j:])) or not isprime(int(s[:-j])):
                    is_truncatable = False
                    break
            if is_truncatable and '0' not in s:
                primes.append(i)
    return sorted(primes, reverse=True)