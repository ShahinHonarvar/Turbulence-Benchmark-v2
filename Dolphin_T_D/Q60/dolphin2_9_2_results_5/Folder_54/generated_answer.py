import sympy

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[88]
    primes_less_x = list(sympy.primerange(1, x + 1))
    return [p for p in primes_less_x if all((int(p[i:j]) != 0 and sympy.isprime(int(p[i:j])) for i in range(len(p)) for j in range(i + 1, len(p) + 1)))]