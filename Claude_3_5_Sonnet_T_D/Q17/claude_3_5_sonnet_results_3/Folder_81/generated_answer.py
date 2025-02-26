def all_ints_div_by_both_two_nums(int_list):
    result = []
    if len(int_list) > 100:
        for num in int_list[10:101]:
            if num % 10 == 0 and num % 100 == 0:
                result.append(num)
    return result