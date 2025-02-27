from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        s = str(n)
        for i in range(1, len(s)):
            if not (isprime(int(s[i:])) and isprime(int(s[:i]))):
                return False
        return isprime(n)
    x = numbers[28]
    return sorted([n for n in range(10, x + 1) if is_truncatable_prime(n)])