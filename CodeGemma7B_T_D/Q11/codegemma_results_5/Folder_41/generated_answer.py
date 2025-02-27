def find_largest_num(num_list):
    max_num = num_list[6]
    for num in num_list[6:]:
        if num > max_num:
            max_num = num
    return max_num