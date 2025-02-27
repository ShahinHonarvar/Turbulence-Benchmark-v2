from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable(n):
        s = str(n)
        return all((isprime(int(s[i:])) and isprime(int(s[:-i] or '0')) for i in range(1, len(s))))
    x = numbers[32]
    return sorted([n for n in range(10, x + 1) if '0' not in str(n) and isprime(n) and is_truncatable(n)])