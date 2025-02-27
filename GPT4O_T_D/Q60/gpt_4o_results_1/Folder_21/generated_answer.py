from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_valid_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        while len(s) > 0:
            if not isprime(int(s)):
                return False
            if len(s) > 1:
                s = s[1:-1]
            else:
                break
        return True
    if len(numbers) <= 175:
        return []
    x = numbers[175]
    left_right_truncatable_primes = []
    for n in range(11, x + 1):
        if is_valid_truncatable(n):
            left_right_truncatable_primes.append(n)
    return left_right_truncatable_primes