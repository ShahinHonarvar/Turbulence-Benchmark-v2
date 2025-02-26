def sum_ints_div_by_either_nums(int_list):
    result = 0
    for num in int_list[11:47]:
        if num % 55 == 0 or num % 36 == 0:
            result += num
    return result