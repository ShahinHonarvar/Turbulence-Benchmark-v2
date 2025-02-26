def all_ints_div_by_both_two_nums(int_list):
    result = []
    for num in int_list[24:33]:
        if num % 35 == 0 and num % 87 == 0:
            result.append(num)
    return result