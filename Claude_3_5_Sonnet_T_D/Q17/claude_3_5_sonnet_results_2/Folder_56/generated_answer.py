def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[7:10]:
        if num % -9 == 0 and num % -7 == 0:
            result.append(num)
    return result