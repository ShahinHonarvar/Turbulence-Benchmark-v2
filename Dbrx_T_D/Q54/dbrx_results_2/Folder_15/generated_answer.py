from sympy import isprime

def all_right_truncatable_prime(x_tuple):
    x = x_tuple[6]
    right_truncatable_primes = []
    for num in range(10, x):
        while num > 0:
            if isprime(num):
                right_truncatable_primes.append(num)
                break
            num = int(str(num)[:-1])
    return sorted(list(set(right_truncatable_primes)), reverse=True) if right_truncatable_primes else []