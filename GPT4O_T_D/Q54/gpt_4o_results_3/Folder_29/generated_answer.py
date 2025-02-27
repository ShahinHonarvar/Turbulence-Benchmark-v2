from sympy import isprime

def all_right_truncatable_prime(numbers):

    def is_right_truncatable(n):
        str_n = str(n)
        while str_n:
            if not isprime(int(str_n)):
                return False
            str_n = str_n[:-1]
        return True
    if len(numbers) < 56:
        return []
    x = numbers[55]
    right_truncatable_primes = []
    for number in range(2, x):
        if is_right_truncatable(number):
            right_truncatable_primes.append(number)
    return sorted(right_truncatable_primes, reverse=True)