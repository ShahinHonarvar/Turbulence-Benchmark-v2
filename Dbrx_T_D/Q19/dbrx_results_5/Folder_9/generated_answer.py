def all_ints_not_div_by_num(input_list):
    result = []
    for i in range(70, 200):
        num = input_list[i]
        if num % -300 != 0:
            result.append(num)
    return result