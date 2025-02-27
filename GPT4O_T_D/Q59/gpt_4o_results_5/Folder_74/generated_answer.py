from sympy import isprime

def all_left_truncatable_prime(numbers):

    def is_left_truncatable(n):
        str_n = str(n)
        while str_n:
            if not isprime(int(str_n)):
                return False
            str_n = str_n[1:]
        return True
    x = numbers[36]
    return sorted((n for n in range(2, x) if '0' not in str(n) and is_left_truncatable(n)))