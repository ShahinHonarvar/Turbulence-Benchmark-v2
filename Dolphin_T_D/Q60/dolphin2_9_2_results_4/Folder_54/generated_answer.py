import sympy

def all_left_right_truncatable_prime(numbers):
    x = numbers[88]
    primes = []
    for n in range(x, 0, -1):
        if sympy.isprime(n):
            str_n = str(n)
            if '0' not in str_n:
                trunc_left = str_n[:-1]
                trunc_right = str_n[1:]
                while trunc_left and sympy.isprime(int(trunc_left)):
                    trunc_left = trunc_left[1:]
                while trunc_right and sympy.isprime(int(trunc_right)):
                    trunc_right = trunc_right[:-1]
                if not (trunc_left or trunc_right):
                    primes.append(n)
    return sorted(primes, reverse=True)