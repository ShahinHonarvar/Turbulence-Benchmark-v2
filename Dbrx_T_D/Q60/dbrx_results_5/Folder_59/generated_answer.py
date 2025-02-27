from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_left_right_truncatable_prime(n):
        if '0' in str(n) or not isprime(n):
            return False
        s = str(n)
        while len(s) > 1:
            s = s[1:] if len(s) > 2 else s[1:]
            if not isprime(int(s)):
                return False
        return True
    x = numbers[84]
    result = [i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)]
    return sorted(result, reverse=True)