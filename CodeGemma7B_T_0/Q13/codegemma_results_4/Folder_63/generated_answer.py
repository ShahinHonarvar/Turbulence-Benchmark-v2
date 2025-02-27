def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 22 or len(num_list) > 88:
        return None
    num_list.sort(reverse=True)
    if num_list[21] == num_list[22]:
        return None
    return num_list[21]