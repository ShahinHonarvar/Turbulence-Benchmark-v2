from sympy import isprime

def all_left_right_truncatable_prime(input_tuple):

    def is_left_truncatable_prime(n):
        if n < 10 and isprime(n):
            return True
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[1:])
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[:-1])
        return True

    def is_left_right_truncatable_prime(n):
        return is_left_truncatable_prime(n) and is_right_truncatable_prime(n)
    x = input_tuple[98]
    result = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)