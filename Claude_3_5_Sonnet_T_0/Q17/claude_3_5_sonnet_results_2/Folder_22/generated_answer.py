def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[40:201]:
        if num % 21 == 0 and num % 71 == 0:
            result.append(num)
    return result