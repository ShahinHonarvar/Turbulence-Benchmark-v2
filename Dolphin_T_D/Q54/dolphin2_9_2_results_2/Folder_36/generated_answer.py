from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[992]
    primes = []
    for i in range(2, x):
        if isprime(i):
            if all((isprime(int(str(i)[:-j])) for j in range(1, len(str(i))))):
                primes.append(i)
    return sorted(primes)