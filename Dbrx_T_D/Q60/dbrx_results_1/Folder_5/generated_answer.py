from sympy import isprime

def all_left_right_truncatable_prime(n_tuple):

    def left_and_right_truncatable_prime(n):
        if '0' in str(n) or not isprime(n):
            return False
        while n > 9:
            n = int(str(n)[1:]) if str(n)[0] == '1' else int(str(n)[:-1])
            if not isprime(n):
                return False
        return True
    x = 10 ** 55 - 1
    for i in n_tuple:
        if i > x:
            x = i
    return sorted([i for i in range(2, x + 1) if left_and_right_truncatable_prime(i)])