from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[69]
    primes = []
    for num in range(2, x):
        if isprime(num):
            trunc = num
            while trunc > 1:
                trunc //= 10
                if not isprime(trunc):
                    break
            else:
                primes.append(num)
    return sorted(primes, reverse=True)