from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        while len(s) > 1:
            s = s[1:-1]
            if s == '':
                return True
            if not isprime(int(s)):
                return False
        return True
    x = numbers[784]
    result = []
    for num in range(2, x + 1):
        if isprime(num) and is_truncatable_prime(num):
            result.append(num)
    return result