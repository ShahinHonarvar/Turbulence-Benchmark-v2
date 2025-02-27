import sympy 

def is_left_truncatable_prime(n):
    if n < 2:
        return False
    while n:
        n = int(n / 10)
        if not sympy.isprime(n):
            return False
    return True

def all_left_truncatable_prime(x):
    left_num = [sympy.primepi(i) for i in range(1, int(str(x))[0] + 1)]
    prime_list = sympy.primerange(2, left_num[-1] + 1)
    return [i for i in prime_list if is_left_truncatable_prime(i) and i < x]