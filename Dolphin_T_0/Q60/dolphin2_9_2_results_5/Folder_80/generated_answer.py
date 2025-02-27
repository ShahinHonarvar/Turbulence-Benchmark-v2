def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[14]
    prime_list = []
    for num in range(x, 0, -1):
        str_num = str(num)
        if '0' in str_num:
            continue
        while len(str_num) > 1:
            if not is_prime(int(str_num)):
                break
            str_num = str_num[1:-1]
        if len(str_num) == 1 and is_prime(int(str_num)):
            prime_list.append(num)
    return sorted(prime_list, reverse=True)