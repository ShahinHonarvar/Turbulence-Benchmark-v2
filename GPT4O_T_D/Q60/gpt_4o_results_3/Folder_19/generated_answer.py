from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        str_n = str(n)
        while len(str_n) > 0:
            if not isprime(int(str_n)) or not isprime(int(str_n[::-1])):
                return False
            str_n = str_n[1:]
        return True
    x = numbers[67]
    return sorted([n for n in range(2, x + 1) if is_truncatable_prime(n)], reverse=True)