from sympy import isprime

def all_left_truncatable_prime(N):
    result = []
    for n in range(2, N + 1):
        if '0' not in str(n) and isprime(n):
            truncatable = True
            for i in range(1, len(str(n))):
                if n % int(str(n)[i:]) != 0 or not isprime(n // int(str(n)[i:])):
                    truncatable = False
                    break
            if truncatable:
                result.append(n)
    return sorted(result)