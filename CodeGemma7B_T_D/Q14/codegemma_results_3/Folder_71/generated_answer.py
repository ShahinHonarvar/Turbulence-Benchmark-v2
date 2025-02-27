def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 52:
        return None
    sliced_list = num_list[26:53]
    sorted_list = sorted(sliced_list)
    if sorted_list[0] == sorted_list[1]:
        return sorted_list[2]
    else:
        return sorted_list[1]