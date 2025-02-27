def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(4):
        num = int_list[i]
        if num % 11 == 0 and num % -7 == 0:
            result.append(num)
    return result