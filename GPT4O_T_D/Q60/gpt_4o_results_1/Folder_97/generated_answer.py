from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(num):
        s = str(num)
        if '0' in s:
            return False
        for i in range(1, len(s)):
            if not (isprime(int(s[i:])) and isprime(int(s[:i]))):
                return False
        return isprime(num)
    x = numbers[645]
    result = []
    for num in range(23, x + 1):
        if is_truncatable_prime(num):
            result.append(num)
    return result