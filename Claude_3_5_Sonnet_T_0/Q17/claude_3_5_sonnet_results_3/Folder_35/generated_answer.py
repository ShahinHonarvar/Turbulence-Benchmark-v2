def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[77:88]:
        if num % 23 == 0 and num % 57 == 0:
            result.append(num)
    return result