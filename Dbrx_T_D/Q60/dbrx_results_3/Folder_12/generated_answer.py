from sympy import isprime

def all_left_right_truncatable_prime(numbers_tuple):

    def is_left_right_truncatable(n):
        if str(n)[0] == '0' or not isprime(n):
            return False
        while n > 10:
            n = int(str(n)[1:])
            if not isprime(n):
                return False
        while n > 0:
            n = int(str(n)[:-1])
            if not isprime(n):
                return False
        return True
    x = max((numbers_tuple[70] for _ in numbers_tuple))
    result = [i for i in range(2, x + 1) if is_left_right_truncatable(i)]
    return sorted(result, reverse=True)