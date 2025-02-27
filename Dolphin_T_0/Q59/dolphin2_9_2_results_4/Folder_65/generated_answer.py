import sympy

def all_left_truncatable_prime(tuple_vals):
    x = tuple_vals[32]
    left_truncatable_primes = []
    for num in range(2, x):
        if sympy.isprime(num) and (not '0' in str(num)):
            trunc = num
            while len(str(trunc)) > 1:
                trunc = int(str(trunc)[1:])
                if not sympy.isprime(trunc):
                    break
            else:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)