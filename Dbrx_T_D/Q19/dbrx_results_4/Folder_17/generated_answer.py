def all_ints_not_div_by_num(integer_list):
    start_index = 39
    end_index = 57
    result = []
    for num in integer_list[start_index:end_index]:
        if num % 84 != 0:
            result.append(num)
    return result