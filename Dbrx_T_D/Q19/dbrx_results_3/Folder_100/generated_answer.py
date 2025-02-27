def all_ints_not_div_by_num(int_list):
    start_index = 62
    end_index = 96
    result = []
    for num in int_list[start_index:end_index]:
        if num % 26 != 0:
            result.append(num)
    return result