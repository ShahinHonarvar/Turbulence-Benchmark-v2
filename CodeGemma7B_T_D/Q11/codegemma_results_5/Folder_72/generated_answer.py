def find_largest_num(num_list):
    max_num = float('-inf')
    for num in num_list[29:52]:
        if num > max_num:
            max_num = num
    return max_num