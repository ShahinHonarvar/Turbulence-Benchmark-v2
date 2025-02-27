from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        while len(str(n)) > 1:
            n = int(str(n)[1:])
            if not isprime(n):
                return False
            n = int(str(n)[:-1])
            if not isprime(n):
                return False
        return True
    return sorted([num for num in numbers if is_left_right_truncatable(num)], reverse=True)