import sympy

def all_left_right_truncatable_prime(numbers):

    def is_left_truncatable_prime(n):
        str_n = str(n)
        while str_n:
            if not sympy.isprime(int(str_n)):
                return False
            str_n = str_n[1:]
        return True

    def is_right_truncatable_prime(n):
        str_n = str(n)
        while str_n:
            if not sympy.isprime(int(str_n)):
                return False
            str_n = str_n[:-1]
        return True
    x = numbers[100]
    result = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_left_truncatable_prime(num) and is_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)