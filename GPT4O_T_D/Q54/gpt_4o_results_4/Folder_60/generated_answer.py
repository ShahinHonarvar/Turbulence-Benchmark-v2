from sympy import isprime

def all_right_truncatable_prime(numbers):

    def is_right_truncatable_prime(n):
        str_n = str(n)
        while str_n:
            if not isprime(int(str_n)):
                return False
            str_n = str_n[:-1]
        return True
    x = numbers[87] if len(numbers) > 87 else 0
    result = [n for n in range(2, x) if is_right_truncatable_prime(n)]
    return sorted(result)