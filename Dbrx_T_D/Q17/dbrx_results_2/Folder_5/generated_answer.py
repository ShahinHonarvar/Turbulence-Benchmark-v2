def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(0, 2):
        num = int_list[i]
        if num % -6 == 0 and num % 4 == 0:
            result.append(num)
    return result