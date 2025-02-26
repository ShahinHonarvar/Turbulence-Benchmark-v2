def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[429]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_valid = True
        str_num = str(num)
        while len(str_num) > 1:
            str_num = str_num[1:]
            if not is_prime(int(str_num)):
                is_valid = False
                break
        str_num = str(num)
        while len(str_num) > 1:
            str_num = str_num[:-1]
            if not is_prime(int(str_num)):
                is_valid = False
                break
        if is_valid and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)