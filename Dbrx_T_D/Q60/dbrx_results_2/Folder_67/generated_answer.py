from sympy import isprime

def all_left_right_truncatable_prime(numbers_tuple):

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        while n > 10:
            n = int(str(n)[1:])
            if not isprime(n):
                return False
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[:-1])
        return True
    x = numbers_tuple[71]
    result = [i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)]
    result.sort(reverse=True)
    return result