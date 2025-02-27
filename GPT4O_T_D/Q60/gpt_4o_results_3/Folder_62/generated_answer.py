from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        str_n = str(n)
        while len(str_n) > 1:
            str_n = str_n[1:-1]
            if str_n and (not isprime(int(str_n))):
                return False
        return True
    x = numbers[70]
    result = []
    for num in range(2, x + 1):
        if isprime(num) and is_truncatable_prime(num):
            result.append(num)
    return result