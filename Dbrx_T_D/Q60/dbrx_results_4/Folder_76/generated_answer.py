from sympy import isprime

def all_left_right_truncatable_prime(n_tuple):
    n = min(10 ** 18, max(1, n_tuple[369]))
    lr_truncatable_primes = []
    for num in range(11, n + 1):
        if not isprime(num):
            continue
        digits = len(str(num))
        for i in range(1, digits):
            if not isprime(int(str(num)[i:])) or not isprime(int(str(num)[:-i])):
                break
        else:
            lr_truncatable_primes.append(num)
    return sorted(lr_truncatable_primes, reverse=True)