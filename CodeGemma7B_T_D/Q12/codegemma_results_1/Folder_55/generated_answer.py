def find_smallest_num(num_list):
    min_num = num_list[0]
    for num in num_list[0:10]:
        if num < min_num:
            min_num = num
    return min_num