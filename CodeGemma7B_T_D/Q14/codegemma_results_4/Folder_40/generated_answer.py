def find_second_smallest_num(num_list):
    if len(num_list) < 3:
        return None
    num_list.sort()
    for num in range(1, 2):
        if num in num_list:
            return num_list[num]