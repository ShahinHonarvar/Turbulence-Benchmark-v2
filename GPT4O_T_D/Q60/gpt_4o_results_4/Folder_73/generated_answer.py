from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            left_truncated = int(str_n[i:])
            right_truncated = int(str_n[:len(str_n) - i])
            if not isprime(left_truncated) or not isprime(right_truncated):
                return False
        return True
    x = numbers[97]
    result = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            result.append(i)
    return sorted(result)