from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[55]
    right_truncatable_primes = []
    for num in range(2, x):
        if all((isprime(int(str(num)[i:])) for i in range(len(str(num))))):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)