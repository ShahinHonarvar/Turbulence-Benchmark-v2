def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(int_tuple):
    x = int_tuple[759]
    prime_list = []
    for num in range(x, 1, -1):
        str_num = str(num)
        if '0' in str_num or not is_prime(num):
            continue
        while len(str_num) > 1:
            if not is_prime(int(str_num[1:])) or not is_prime(int(str_num[:-1])):
                break
            str_num = str_num[1:]
            str_num = str_num[:-1]
        if len(str_num) == 1 and is_prime(int(str_num)):
            prime_list.append(num)
    return sorted(prime_list, reverse=True)