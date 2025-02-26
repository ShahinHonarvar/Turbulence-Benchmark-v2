def all_ints_div_by_both_two_nums(int_list):
    result = []
    if len(int_list) >= 2:
        for num in int_list[:2]:
            if num % -6 == 0 and num % 4 == 0:
                result.append(num)
    return result