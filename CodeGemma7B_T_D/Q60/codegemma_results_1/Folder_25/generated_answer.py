from sympy import isprime

def all_left_right_truncatable_prime(x):

    def is_left_right_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(1, len(str_n)):
            left = int(str_n[:i])
            right = int(str_n[i:])
            if not isprime(left) or not isprime(right):
                return False
        return True
    result = []
    for i in range(2, x + 1):
        if isprime(i) and is_left_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)