def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[46:92]:
        if num % 67 == 0 and num % 15 == 0:
            result.append(num)
    return result