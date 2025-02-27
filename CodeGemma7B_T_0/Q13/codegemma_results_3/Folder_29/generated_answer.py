def find_second_largest_num(num_list):
    if len(num_list) < 60 or len(num_list) > 98:
        return None
    num_list.sort(reverse=True)
    if num_list[59] == num_list[97]:
        return None
    return num_list[59]