def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[31:51]:
        if num % 81 == 0 and num % 64 == 0:
            result.append(num)
    return result