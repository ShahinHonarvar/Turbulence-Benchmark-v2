from sympy import isprime

def all_right_truncatable_prime(x_tuple):
    x = x_tuple[1]
    right_truncatable_primes = []
    for i in range(1, x):
        if isprime(i):
            is_right_truncatable = True
            while i > 1:
                if not isprime(i):
                    is_right_truncatable = False
                    break
                i = i * 10 + int(str(i)[-1])
            if is_right_truncatable:
                right_truncatable_primes.append(i)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes