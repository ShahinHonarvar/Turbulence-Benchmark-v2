def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_right_truncate(num):
    str_num = str(num)
    left_truncatable = all((is_prime(int(str_num[i:])) for i in range(len(str_num))))
    right_truncatable = all((is_prime(int(str_num[:i])) for i in range(1, len(str_num))))
    return left_truncatable and right_truncatable

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[0]
    truncatable_primes = []
    for num in range(x, 0, -1):
        if str(num).count('0') == 0 and is_prime(num) and left_right_truncate(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)