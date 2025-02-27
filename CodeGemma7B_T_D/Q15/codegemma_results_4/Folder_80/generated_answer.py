def sum_odd_ints_inclusive(int_list):
    odd_nums = 0
    for num in int_list[64:67]:
        if num % 2 != 0:
            odd_nums += num
    return odd_nums if odd_nums else 0