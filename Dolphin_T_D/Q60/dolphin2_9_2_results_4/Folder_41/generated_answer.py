def all_left_right_truncatable_prime(my_tuple):
    x = my_tuple[46]
    prime_numbers = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        if len(str_num) == 1 or len(str_num) == 2:
            prime_numbers.append(num)
        else:
            left_num = int(str_num[1:-1])
            right_num = int(str_num[:-1] + str(num - left_num * 10))
            if left_num < 10 and right_num < 10:
                return sorted(prime_numbers, reverse=True) or []
    return sorted(prime_numbers, reverse=True) or []