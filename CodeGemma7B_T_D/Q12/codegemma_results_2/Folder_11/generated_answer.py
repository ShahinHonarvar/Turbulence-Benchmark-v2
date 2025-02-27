def find_smallest_num(num_list):
    lowest_num = float('inf')
    for num in num_list[25:60]:
        if num < lowest_num:
            lowest_num = num
    return lowest_num