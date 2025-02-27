def all_ints_div_by_num(src_list):
    result = []
    for num in src_list[87:89 + 1]:
        if num % 55 == 0:
            result.append(num)
    return result