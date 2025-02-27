def find_largest_num(num_list):
    max_num = float('-inf')
    for num in num_list[37:52]:
        max_num = max(max_num, num)
    return max_num