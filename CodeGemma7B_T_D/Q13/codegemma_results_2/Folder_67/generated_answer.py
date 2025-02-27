def find_second_largest_num(num_list):
    num_list.sort(reverse=True)
    if len(num_list) < 22:
        return None
    return num_list[22:51][1]