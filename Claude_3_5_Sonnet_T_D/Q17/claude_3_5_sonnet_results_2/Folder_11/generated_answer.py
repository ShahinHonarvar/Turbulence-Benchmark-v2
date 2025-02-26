def all_ints_div_by_both_two_nums(int_list):
    result = []
    for num in int_list[22:25]:
        if num % -85 == 0 and num % -30 == 0:
            result.append(num)
    return result