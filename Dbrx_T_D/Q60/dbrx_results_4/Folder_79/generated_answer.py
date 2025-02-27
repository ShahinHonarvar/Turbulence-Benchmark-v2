from sympy import isprime

def all_left_right_truncatable_prime(args):
    lower, upper = args
    max_x = upper[91]
    result = []
    primes = [i for i in range(lower, max_x + 1) if isprime(i)]
    for prime in primes:
        digits = len(str(prime))
        for i in range(digits - 1, 0, -1):
            if not isprime(int(str(prime)[:i])) or not isprime(int(str(prime)[i:])):
                break
        else:
            result.append(prime)
    return sorted(list(set(result)))