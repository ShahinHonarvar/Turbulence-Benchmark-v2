from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        s = str(n)
        while len(s) > 1:
            s = s[1:-1]
            if s and (not isprime(int(s))):
                return False
        return True
    x = numbers[54]
    result = []
    for num in range(11, x + 1):
        if '0' not in str(num) and isprime(num) and is_truncatable_prime(num):
            result.append(num)
    return result