def all_ints_div_by_both_two_nums(int_list):
    result = []
    for num in int_list[25:96]:
        if num % 51 == 0 and num % 77 == 0:
            result.append(num)
    return result