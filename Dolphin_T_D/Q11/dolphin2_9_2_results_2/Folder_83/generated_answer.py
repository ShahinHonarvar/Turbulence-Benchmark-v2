def find_largest_num(num_list):
    max_num = num_list[90]
    for num in num_list[90:201]:
        if num > max_num:
            max_num = num
    return max_num