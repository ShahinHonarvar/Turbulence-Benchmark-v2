import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.sqrt(n))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(arguments):
    x = arguments[126]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        while len(str_num) > 2 and is_prime(int(str_num)):
            str_num = str_num[1:-1]
            if len(str_num) == 1 or (len(str_num) == 2 and is_prime(int(str_num))):
                left_right_truncatable_primes.append(num)
                break
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes