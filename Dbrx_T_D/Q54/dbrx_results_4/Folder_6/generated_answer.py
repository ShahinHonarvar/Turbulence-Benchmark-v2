from sympy import isprime

def all_right_truncatable_prime(num_tuple):
    x = num_tuple[74]
    right_truncatable_primes = []
    for i in range(10, x):
        if isprime(i):
            j = i // 10
            while j > 0:
                if not isprime(j):
                    break
                j = j // 10
            else:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)