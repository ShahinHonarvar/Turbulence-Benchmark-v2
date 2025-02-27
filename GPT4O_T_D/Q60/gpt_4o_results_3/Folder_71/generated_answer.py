from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[22]

    def is_truncatable_prime(n):
        s = str(n)
        while len(s) > 1:
            s = s[1:-1]
            if not s or not isprime(int(s)):
                return False
        return True
    result = [n for n in range(11, x + 1) if '0' not in str(n) and isprime(n) and is_truncatable_prime(n)]
    return sorted(result, reverse=True)