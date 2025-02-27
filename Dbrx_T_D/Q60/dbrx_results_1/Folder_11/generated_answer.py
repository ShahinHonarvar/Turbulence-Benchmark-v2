from sympy import isprime

def all_left_right_truncatable_prime(args):

    def is_left_right_truncatable_prime(n):
        if n < 10:
            return isprime(n)
        if '0' in str(n):
            return False
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[1:]) if n < 100 else int(str(n)[:-1])
        return True
    x = 1009
    result = []
    for num in range(1, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return result