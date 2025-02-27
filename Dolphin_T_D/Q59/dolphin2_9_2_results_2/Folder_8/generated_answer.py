def all_left_truncatable_prime(arg):
    x = arg[41]
    left_truncatable_list = []
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            str_num = str(num)
            i = 0
            while i < len(str_num) and int(str_num) % num != 0:
                str_num = str_num[1:]
                i += 1
            if len(str_num) == 0 or int(str_num) == 0 or int(str_num) % num != 0:
                left_truncatable_list.append(num)
    return sorted(left_truncatable_list, reverse=True)