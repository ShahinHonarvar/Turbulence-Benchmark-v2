def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[42:44]:
        if num % 15 == 0 and num % 87 == 0:
            result.append(num)
    return result