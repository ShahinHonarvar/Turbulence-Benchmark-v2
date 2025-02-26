def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[240:902]:
        if num % 546 == 0 and num % 709 == 0:
            result.append(num)
    return result