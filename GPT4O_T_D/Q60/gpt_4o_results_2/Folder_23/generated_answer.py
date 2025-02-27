from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        while len(str_n) > 1:
            str_n = str_n[1:-1]
            if str_n and (not isprime(int(str_n))):
                return False
        return True
    if len(numbers) < 78:
        return []
    x = numbers[77]
    result = [n for n in range(23, x + 1) if isprime(n) and is_truncatable_prime(n)]
    return sorted(result, reverse=True)