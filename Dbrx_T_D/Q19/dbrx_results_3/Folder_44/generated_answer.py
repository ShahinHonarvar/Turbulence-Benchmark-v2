def all_ints_not_div_by_num(input_list):
    result = []
    for i in range(46, 91):
        num = input_list[i]
        if num % 67 != 0:
            result.append(num)
    return result