def all_ints_div_by_both_two_nums(int_list):
    result = []
    for num in int_list[1:5]:
        if num % 4 == 0 and num % -6 == 0:
            result.append(num)
    return result