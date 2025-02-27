from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[74]
    primes = []
    for i in range(1, x):
        if isprime(i):
            prime = str(i)
            is_right_truncatable = True
            for j in range(len(prime)):
                if not isprime(int(prime[j:])):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                primes.append(i)
    return sorted(primes)