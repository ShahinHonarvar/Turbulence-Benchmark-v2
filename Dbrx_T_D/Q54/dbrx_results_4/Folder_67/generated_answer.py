from sympy import isprime

def all_right_truncatable_prime(tup):
    primes = []
    for i in range(tup[70]):
        if isprime(i):
            is_right_truncatable = True
            for j in str(i):
                if not isprime(int(''.join(str(i)[:int(j)]))):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)