from sympy import isprime

def all_left_right_truncatable_prime(n):

    def is_left_right_truncatable_prime(k):
        while k > 9:
            if str(k)[0] == '0' or not isprime(k):
                return False
            k = int(str(k)[1:]) if k > 99 else int(str(k)[1:])
        return True
    x, y = (1, 1)
    result = []
    while x <= n:
        if is_left_right_truncatable_prime(x):
            if isprime(x) and '0' not in str(x):
                result.append(x)
        x, y = (x + y, y + y + 1)
    return result[::-1]