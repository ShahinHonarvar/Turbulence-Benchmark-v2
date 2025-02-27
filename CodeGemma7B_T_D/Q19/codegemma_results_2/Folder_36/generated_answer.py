def all_ints_not_div_by_num(num_list):
    filtered_nums = []
    for num in num_list[472:827]:
        if num % 602 != 0:
            filtered_nums.append(num)
    return filtered_nums