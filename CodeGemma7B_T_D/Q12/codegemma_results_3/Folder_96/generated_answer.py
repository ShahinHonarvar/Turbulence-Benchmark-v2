def find_smallest_num(num_list):
    small = float('inf')
    for num in num_list[50:201]:
        if small > num:
            small = num
    return small