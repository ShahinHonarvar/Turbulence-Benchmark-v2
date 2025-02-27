def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 799:
        return 0
    start_index, end_index = (154, 798)
    total = 0
    for num in int_list[start_index:end_index + 1]:
        if num % 275 == 0 or num % 580 == 0:
            total += num
    return total