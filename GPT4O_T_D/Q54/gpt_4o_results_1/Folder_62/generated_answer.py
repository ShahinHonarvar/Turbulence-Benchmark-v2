from sympy import isprime

def right_truncatable_primes(n):
    result = []
    for i in range(2, n):
        num = i
        is_truncatable = True
        while num > 0:
            if not isprime(num):
                is_truncatable = False
                break
            num //= 10
        if is_truncatable:
            result.append(i)
    return result

def all_right_truncatable_prime(t):
    if len(t) <= 70:
        return []
    x = t[70]
    primes = right_truncatable_primes(x)
    return sorted(primes)