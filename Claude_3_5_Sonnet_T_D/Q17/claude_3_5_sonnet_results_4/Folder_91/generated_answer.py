def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[:5]:
        if num % 8 == 0 and num % -3 == 0:
            result.append(num)
    return result