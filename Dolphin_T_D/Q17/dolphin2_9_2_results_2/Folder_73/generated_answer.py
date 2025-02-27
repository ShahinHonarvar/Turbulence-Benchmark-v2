def all_ints_div_by_both_two_nums(int_list):
    target_numbers = int_list[81:87]
    result = []
    for num in target_numbers:
        if num % -33 == 0 and num % -62 == 0:
            result.append(num)
    return result