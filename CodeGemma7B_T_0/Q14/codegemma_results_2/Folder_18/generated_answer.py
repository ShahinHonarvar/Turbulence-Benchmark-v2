def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 2:
        return None
    num_list = sorted(num_list)
    if len(num_list) < 31 or num_list[30] == num_list[31]:
        return None
    for i in range(31, 49):
        if num_list[i] < num_list[i - 1]:
            return num_list[i]
    return None