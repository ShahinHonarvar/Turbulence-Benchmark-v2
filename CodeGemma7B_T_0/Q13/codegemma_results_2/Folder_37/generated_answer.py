def find_second_largest_num(num_list):
    if len(num_list) < 2 or max(num_list) < 1 or min(num_list) > 5:
        return None
    num_list.sort(reverse=True)
    for i in range(1, 6):
        if num_list[i] != max(num_list):
            return num_list[i]
    return None