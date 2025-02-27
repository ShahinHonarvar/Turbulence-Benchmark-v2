def all_ints_div_by_num(num_list):
    result = []
    for num in num_list[45:81]:
        if num % 39 == 0:
            result.append(num)
    return result