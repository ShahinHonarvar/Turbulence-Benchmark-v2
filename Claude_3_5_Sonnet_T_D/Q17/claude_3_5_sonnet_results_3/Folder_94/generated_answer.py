def all_ints_div_by_both_two_nums(int_list):
    result = []
    for num in int_list[93:95]:
        if num % -53 == 0 and num % -91 == 0:
            result.append(num)
    return result