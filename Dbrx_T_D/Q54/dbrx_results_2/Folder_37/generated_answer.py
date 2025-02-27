from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[35]
    right_trunc_primes = []
    for i in range(10, x):
        j = i
        while j > 0:
            if not isprime(j):
                break
            j = j // 10
        if j == 0:
            right_trunc_primes.append(i)
    right_trunc_primes.sort(reverse=True)
    return right_trunc_primes