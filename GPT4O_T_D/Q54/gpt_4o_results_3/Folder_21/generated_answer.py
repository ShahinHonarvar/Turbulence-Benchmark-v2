import sympy

def all_right_truncatable_prime(numbers):

    def is_right_truncatable_prime(n):
        if n < 2:
            return False
        str_n = str(n)
        while str_n:
            if not sympy.isprime(int(str_n)):
                return False
            str_n = str_n[:-1]
        return True
    x = numbers[175]
    result = [n for n in range(2, x) if is_right_truncatable_prime(n)]
    return sorted(result)