from sympy import isprime

def all_right_truncatable_prime(x_tuple):
    x = x_tuple[792]
    rt_primes = []
    for num in range(1, x):
        while num > 0:
            if isprime(num):
                rt_primes.append(num)
                break
            else:
                num = num // 10
    return sorted(list(set(rt_primes)))