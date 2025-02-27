from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        s = str(n)
        for i in range(len(s)):
            if not isprime(int(s[i:])) or not isprime(int(s[:len(s) - i])):
                return False
        return True
    x = numbers[14]
    truncatable_primes = [i for i in range(10, x + 1) if '0' not in str(i) and is_truncatable_prime(i)]
    return sorted(truncatable_primes, reverse=True)