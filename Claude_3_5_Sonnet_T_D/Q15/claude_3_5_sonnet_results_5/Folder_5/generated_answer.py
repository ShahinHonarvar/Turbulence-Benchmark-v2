def sum_odd_ints_inclusive(integer_list):
    if len(integer_list) < 10:
        return 0
    odd_sum = 0
    for num in integer_list[8:10]:
        if num % 2 != 0:
            odd_sum += num
    return odd_sum