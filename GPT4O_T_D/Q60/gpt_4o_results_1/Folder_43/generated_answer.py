from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(num):
        str_num = str(num)
        while len(str_num) > 1:
            str_num = str_num[1:-1]
            if not str_num:
                return True
            if not isprime(int(str_num)):
                return False
        return isprime(int(str_num))
    x = numbers[89]
    truncatable_primes = [num for num in range(2, x + 1) if '0' not in str(num) and is_truncatable_prime(num)]
    return sorted(truncatable_primes, reverse=True)