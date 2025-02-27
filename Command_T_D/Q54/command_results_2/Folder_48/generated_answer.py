import sys

def all_right_truncatable_prime(test_case):
    primes = []
    primes_str = input(test_case).split()
    for prime in primes_str:
        if int(prime) < 10 ** 9:
            primes.append(int(prime))

    def is_right_truncatable(n):
        if all((n % i != 0 for i in range(2, int(n ** 0.5) + 1))):
            return True
        for i in range(int(n ** 0.5) + 1):
            if n % i == 0:
                break
            else:
                return True
        return False
    right_truncatable_primes = []
    for prime in primes:
        if is_right_truncatable(prime):
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes)