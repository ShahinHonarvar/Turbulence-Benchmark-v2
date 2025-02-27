def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 81:
        return 0
    result = 0
    for num in int_list[80:201]:
        if num % 10 == 0 or num % 1000 == 0:
            result += num
    return result