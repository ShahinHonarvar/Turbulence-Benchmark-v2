def sum_odd_ints_inclusive(list):
    odd_nums = 0
    for num in list[22:52]:
        if num % 2 != 0:
            odd_nums += num
    return odd_nums or 0