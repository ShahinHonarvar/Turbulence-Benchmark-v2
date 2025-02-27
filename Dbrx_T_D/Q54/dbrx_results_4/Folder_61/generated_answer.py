from sympy import isprime

def all_right_truncatable_prime(args):
    x = args[3]
    primes = []
    for i in range(1, x):
        if isprime(i):
            is_right_truncatable = True
            for j in range(len(str(i)) - 1):
                if not isprime(int(str(i)[:-j - 1])):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)