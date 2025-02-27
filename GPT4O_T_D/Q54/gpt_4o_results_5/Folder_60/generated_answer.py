from sympy import isprime

def all_right_truncatable_prime(numbers):

    def is_right_truncatable(prime):
        prime_str = str(prime)
        while prime_str:
            if not isprime(int(prime_str)):
                return False
            prime_str = prime_str[:-1]
        return True
    x = numbers[87]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_right_truncatable(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)