import sympy

def all_left_right_truncatable_prime(numbers):

    def is_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(1, len(str_n)):
            if not sympy.isprime(int(str_n[i:])) or not sympy.isprime(int(str_n[:i])):
                return False
        return True
    x = numbers[32]
    truncatable_primes = []
    for num in range(11, x + 1):
        if sympy.isprime(num) and is_truncatable(num):
            truncatable_primes.append(num)
    return truncatable_primes