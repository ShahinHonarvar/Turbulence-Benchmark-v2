def all_ints_div_by_both_two_nums(int_list):
    result = []
    for num in int_list[2:8]:
        if num % -1 == 0 and num % -7 == 0:
            result.append(num)
    return result