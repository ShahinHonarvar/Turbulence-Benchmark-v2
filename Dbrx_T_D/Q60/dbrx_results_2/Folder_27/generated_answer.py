from sympy import isprime

def all_left_right_truncatable_prime(nums_tuple):
    x = nums_tuple[79]
    primes = [i for i in range(2, x + 1) if isprime(i)]
    ltr_primes = []
    for prime in primes:
        digits = len(str(prime))
        if digits > 1:
            for i in range(1, digits):
                if not isprime(int(str(prime)[:i])) or not isprime(int(str(prime)[i:])):
                    break
            else:
                ltr_primes.append(prime)
    return sorted(ltr_primes, reverse=True)