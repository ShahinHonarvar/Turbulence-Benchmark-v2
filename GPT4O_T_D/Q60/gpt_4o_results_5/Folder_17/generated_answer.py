from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_left_right_truncatable_prime(num):
        str_num = str(num)
        while len(str_num) > 1:
            str_num = str_num[1:-1]
            if not str_num:
                return True
            if not isprime(int(str_num)) or '0' in str_num:
                return False
        return isprime(num)
    x = numbers[36]
    return sorted([num for num in range(2, x + 1) if isprime(num) and is_left_right_truncatable_prime(num)], reverse=True)