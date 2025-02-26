def sum_ints_div_by_either_nums(int_list):
    if len(int_list) <= 200:
        return 0
    result = 0
    for num in int_list[200:201]:
        if num % 17 == 0 or num % -5 == 0:
            result += num
    return result