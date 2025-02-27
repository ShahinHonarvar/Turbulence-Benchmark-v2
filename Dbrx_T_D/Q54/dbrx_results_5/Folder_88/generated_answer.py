from sympy import isprime

def all_right_truncatable_prime(num_tuple):
    x = num_tuple[93]
    right_truncatable_primes = []
    for num in range(1, x):
        while num > 0:
            if isprime(num):
                right_truncatable_primes.append(num)
                break
            num = num // 10
    return sorted(list(set(right_truncatable_primes)))