from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        s = str(n)
        for k in range(1, len(s)):
            if not isprime(int(s[k:])) or not isprime(int(s[:-k])):
                return False
        return True
    x = numbers[73]
    truncatable_primes = [num for num in range(10, x + 1) if isprime(num) and is_truncatable_prime(num)]
    return sorted(truncatable_primes, reverse=True)