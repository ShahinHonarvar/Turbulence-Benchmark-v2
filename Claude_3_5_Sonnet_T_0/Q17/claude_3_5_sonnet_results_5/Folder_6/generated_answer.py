def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[41:57]:
        if num % 82 == 0 and num % 90 == 0:
            result.append(num)
    return result