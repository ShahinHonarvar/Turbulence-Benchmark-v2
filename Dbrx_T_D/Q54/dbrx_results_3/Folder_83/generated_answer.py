from sympy import isprime

def all_right_truncatable_prime(x_tuple):
    x = x_tuple[24]
    rt_primes = []
    for num in range(1, x):
        if isprime(num):
            is_rt_prime = True
            while num > 0:
                if not isprime(num):
                    is_rt_prime = False
                    break
                num = int(str(num)[:-1])
            if is_rt_prime:
                rt_primes.append(num)
    return sorted(list(set(rt_primes)))