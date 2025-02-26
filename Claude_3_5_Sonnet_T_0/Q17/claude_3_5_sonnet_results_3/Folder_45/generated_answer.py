def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[30:201]:
        if num % -115 == 0 and num % 115 == 0:
            result.append(num)
    return result