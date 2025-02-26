def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[78:82]:
        if num % 76 == 0 and num % 60 == 0:
            result.append(num)
    return result