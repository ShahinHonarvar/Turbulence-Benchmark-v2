from sympy import isprime

def all_right_truncatable_prime(nums_tuple):
    x = nums_tuple[36]
    rt_primes = []
    for num in range(10, x):
        if isprime(num):
            while num > 0:
                if not isprime(num):
                    break
                num = num // 10
            else:
                rt_primes.append(num)
    rt_primes.sort(reverse=True)
    return rt_primes