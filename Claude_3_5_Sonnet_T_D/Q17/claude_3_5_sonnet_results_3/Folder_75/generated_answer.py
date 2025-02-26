def all_ints_div_by_both_two_nums(int_list):
    result = []
    for num in int_list[20:94]:
        if num % -92 == 0 and num % -50 == 0:
            result.append(num)
    return result