def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[11:47]:
        if num % 55 == 0 and num % 36 == 0:
            result.append(num)
    return result