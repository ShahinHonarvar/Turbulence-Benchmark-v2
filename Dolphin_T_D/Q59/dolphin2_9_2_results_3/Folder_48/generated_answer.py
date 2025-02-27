import sympy

def all_left_truncatable_prime(int_tuple):
    x = int_tuple[835]
    left_trunc_primes = []
    for num in sympy.primerange(1, x):
        str_num = str(num)
        while len(str_num) != 0:
            if sympy.isprime(int(str_num)):
                str_num = str_num[1:]
            else:
                break
        if len(str_num) == 0:
            left_trunc_primes.append(num)
    return sorted(left_trunc_primes)