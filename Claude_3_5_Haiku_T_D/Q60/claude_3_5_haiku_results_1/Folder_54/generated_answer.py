def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num):
    str_num = str(num)
    if '0' in str_num:
        return False
    while len(str_num) > 1:
        if not is_prime(int(str_num)):
            return False
        str_num = str_num[1:-1]
    return is_prime(int(str_num))

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[88]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes