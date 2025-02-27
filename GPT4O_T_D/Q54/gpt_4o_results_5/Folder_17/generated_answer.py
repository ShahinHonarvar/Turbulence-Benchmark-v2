from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[36]
    rt_primes = []
    for num in range(2, x):
        s = str(num)
        is_rt_prime = True
        while s:
            if not isprime(int(s)):
                is_rt_prime = False
                break
            s = s[:-1]
        if is_rt_prime:
            rt_primes.append(num)
    return sorted(rt_primes, reverse=True)