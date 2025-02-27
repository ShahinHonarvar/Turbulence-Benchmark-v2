import sympy

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[30]
    left_truncatable_primes = []
    for num in range(2, x):
        if sympy.isprime(num) and (not '0' in str(num)):
            valid = True
            for i in range(len(str(num)) - 1, 0, -1):
                if not sympy.isprime(int(str(num)[i:])):
                    valid = False
                    break
            if valid:
                left_truncatable_primes.append(num)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes