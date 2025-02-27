def find_largest_num(num_list):
    max_num = num_list[0]
    for num in num_list[1:]:
        if num > max_num:
            max_num = num
    return max_num