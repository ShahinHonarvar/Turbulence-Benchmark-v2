from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[18]
    left_truncatable_primes = []
    for i in range(1, x):
        if isprime(i):
            is_left_truncatable = True
            for j in str(i):
                if not isprime(int(j)):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)