import sympy

def all_right_truncatable_prime(tup):
    primes = []
    for num in range(10, sympy.nextprime(tup[85])):
        if sympy.isprime(num):
            is_right_truncatable = True
            while num > 9:
                if not sympy.isprime(int(str(num)[1:])):
                    is_right_truncatable = False
                    break
                num = int(str(num)[:-1])
            if is_right_truncatable:
                primes.append(num)
    return sorted(primes)