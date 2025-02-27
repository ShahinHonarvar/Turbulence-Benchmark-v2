def all_ints_div_by_both_two_nums(int_list):
    result = []
    for num in int_list[14:94]:
        if num % 71 == 0 and num % 81 == 0:
            result.append(num)
    return result