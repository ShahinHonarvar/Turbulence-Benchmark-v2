import sympy

def all_left_right_truncatable_prime(numbers):
    x = numbers[55]

    def is_truncatable_prime(n):
        s = str(n)
        for i in range(len(s)):
            if not sympy.isprime(int(s[i:])) or not sympy.isprime(int(s[:i + 1])):
                return False
        return '0' not in s
    return sorted([n for n in range(10, x + 1) if is_truncatable_prime(n)])