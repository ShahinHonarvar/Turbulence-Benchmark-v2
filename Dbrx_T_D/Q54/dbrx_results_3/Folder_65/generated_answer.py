from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[32]
    r_primes = []
    for i in range(1, 10):
        if isprime(i):
            r_primes.append(int(i))
    for j in range(2, int(x ** 0.5) + 1):
        if j in r_primes:
            r_primes.append(int(str(j) + '0'))
            for k in range(1, 10):
                if isprime(int(str(j) + str(k))):
                    r_primes.append(int(str(j) + str(k)))
    r_primes = [num for num in r_primes if num < x]
    r_primes.sort()
    return r_primes