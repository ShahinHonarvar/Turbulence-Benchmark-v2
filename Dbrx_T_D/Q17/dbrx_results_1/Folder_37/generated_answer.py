def all_ints_div_by_both_two_nums(input_list):
    if len(input_list) < 8:
        return []
    result = []
    for i in range(2, 8):
        num = input_list[i]
        if num % -1 == 0 and num % -7 == 0:
            result.append(num)
    return result