from sympy import isprime

def all_right_truncatable_prime(numbers):

    def is_right_truncatable_prime(n):
        if not isprime(n):
            return False
        str_n = str(n)
        while len(str_n) > 1:
            str_n = str_n[:-1]
            if not isprime(int(str_n)):
                return False
        return True
    x = numbers[79]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)