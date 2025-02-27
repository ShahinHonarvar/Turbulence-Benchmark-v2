def find_largest_num(num_list):
    large_num = float('-inf')
    for num in num_list[54:99]:
        large_num = max(large_num, num)
    return large_num