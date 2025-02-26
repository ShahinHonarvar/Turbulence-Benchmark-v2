def sum_ints_div_by_either_nums(integer_list):
    result = 0
    for num in integer_list[18:53]:
        if num % 15 == 0 or num % 57 == 0:
            result += num
    return result