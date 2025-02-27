def find_smallest_num(num_list):
    smallest_num = num_list[0]
    for num in num_list[0:7]:
        if num < smallest_num:
            smallest_num = num
    return smallest_num