def all_ints_not_div_by_num(num_list):
    if len(num_list) <= 72:
        return []
    filtered_nums = []
    for num in num_list[63:73]:
        if num % -99 != 0:
            filtered_nums.append(num)
    return filtered_nums