from sympy import isprime

def all_left_truncatable_prime(numbers):

    def is_left_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):
            if not isprime(int(s[i:])):
                return False
        return True
    x = numbers[20]
    result = [n for n in range(2, x) if is_left_truncatable_prime(n)]
    return sorted(result, reverse=True)