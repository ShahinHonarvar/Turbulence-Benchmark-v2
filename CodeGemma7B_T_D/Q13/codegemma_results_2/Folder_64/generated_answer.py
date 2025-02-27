def find_second_largest_num(num_list):
    if not num_list:
        return None
    if len(num_list) <= 1:
        return None
    num_list.sort(reverse=True)
    if num_list[0] == num_list[1]:
        return None
    return num_list[1]