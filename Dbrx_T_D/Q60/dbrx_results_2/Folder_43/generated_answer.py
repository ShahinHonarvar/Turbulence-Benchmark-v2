from sympy import isprime

def all_left_right_truncatable_prime(numbers_tuple):

    def is_left_and_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        while n > 10 and isprime(n):
            n = int(str(n)[1:])
            if not isprime(n):
                return False
        while n > 9 and isprime(n):
            n = int(str(n)[:-1])
            if not isprime(n):
                return False
        return isprime(n)
    target = max(numbers_tuple)
    return sorted([num for num in range(2, target + 1) if is_left_and_right_truncatable_prime(num)], reverse=True)