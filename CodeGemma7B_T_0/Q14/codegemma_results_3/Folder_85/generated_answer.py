def find_second_smallest_num(num_list):
    if len(num_list) < 2 or max(num_list) - min(num_list) < 2:
        return None
    num_list.sort()
    for i in range(len(num_list)):
        if i >= 0 and i <= 6 and (num_list[i] != num_list[0]):
            return num_list[i]
    return None