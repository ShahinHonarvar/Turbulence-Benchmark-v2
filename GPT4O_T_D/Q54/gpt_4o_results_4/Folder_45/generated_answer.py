from sympy import isprime

def all_right_truncatable_prime(numbers):

    def is_right_truncatable_prime(num):
        str_num = str(num)
        while str_num:
            if not isprime(int(str_num)):
                return False
            str_num = str_num[:-1]
        return True
    x = numbers[61]
    result = [n for n in range(2, x) if is_right_truncatable_prime(n)]
    return sorted(result)