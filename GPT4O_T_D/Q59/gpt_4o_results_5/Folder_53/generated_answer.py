from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[86]

    def is_left_truncatable_prime(num):
        str_num = str(num)
        while str_num:
            if '0' in str_num or not isprime(int(str_num)):
                return False
            str_num = str_num[1:]
        return True
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n)], reverse=True)