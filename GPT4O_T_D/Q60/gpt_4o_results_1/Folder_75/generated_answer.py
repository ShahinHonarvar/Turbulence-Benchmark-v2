from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):
            if not isprime(int(s[i:])) or not isprime(int(s[:len(s) - i])):
                return False
        return True
    x = numbers[41]
    result = [n for n in range(10, x + 1) if is_truncatable_prime(n)]
    return sorted(result)