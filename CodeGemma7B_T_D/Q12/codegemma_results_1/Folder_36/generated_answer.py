def find_smallest_num(num_list):
    smallest_num = float('inf')
    for num in num_list[310:371]:
        if num < smallest_num:
            smallest_num = num
    return smallest_num