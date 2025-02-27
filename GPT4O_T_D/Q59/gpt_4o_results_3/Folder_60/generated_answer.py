from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[87]

    def is_left_truncatable_prime(n):
        if '0' in str(n) or not isprime(n):
            return False
        s = str(n)
        while len(s) > 1:
            s = s[1:]
            if not isprime(int(s)):
                return False
        return True
    result = [n for n in range(2, x) if is_left_truncatable_prime(n)]
    return result