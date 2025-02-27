import sympy

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        s = str(n)
        while len(s) > 1:
            s = s[1:-1]
            if not s:
                break
            if not sympy.isprime(int(s)):
                return False
        return True
    truncatable_primes = []
    x = numbers[93]
    for num in range(2, x + 1):
        if sympy.isprime(num) and '0' not in str(num):
            if is_truncatable_prime(num):
                truncatable_primes.append(num)
    return truncatable_primes