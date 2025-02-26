def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[3:10]:
        if num % 6 == 0 and num % 1 == 0:
            result.append(num)
    return result