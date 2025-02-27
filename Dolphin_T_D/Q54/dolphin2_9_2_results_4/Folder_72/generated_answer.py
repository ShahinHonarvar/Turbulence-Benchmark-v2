import math

def all_right_truncatable_prime(t):
    x = t[31]
    prime_numbers = [i for i in range(2, x) if all((i % j != 0 for j in range(2, int(math.sqrt(i)) + 1))) and i != 1]
    right_truncatable_primes = [i for i in prime_numbers if all((int(str(i)[-j]) in prime_numbers for j in range(1, len(str(i)))))]
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes