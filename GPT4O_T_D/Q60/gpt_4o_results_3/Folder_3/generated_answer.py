from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable(p):
        if '0' in str(p):
            return False
        s = str(p)
        while len(s) > 1:
            s = s[1:-1]
            if not s or not isprime(int(s)):
                return False
        return True
    x = numbers[100]
    result = []
    for num in range(2, x + 1):
        if isprime(num) and is_truncatable(num):
            result.append(num)
    return sorted(result)