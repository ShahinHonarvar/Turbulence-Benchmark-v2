from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_left_right_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            left_truncation = int(str_n[i:])
            right_truncation = int(str_n[:-i]) if i > 0 else n
            if not isprime(left_truncation) or not isprime(right_truncation):
                return False
        return True
    x = numbers[19]
    result = []
    for i in range(10, x + 1):
        if isprime(i) and is_left_right_truncatable(i):
            result.append(i)
    return sorted(result)