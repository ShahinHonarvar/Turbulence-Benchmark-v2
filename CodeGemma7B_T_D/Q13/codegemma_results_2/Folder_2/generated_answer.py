def find_second_largest_num(num_list):
    num_list.sort(reverse=True)
    if len(num_list) <= 39 or max(num_list[:15]) == max(num_list[39:]):
        return None
    return num_list[39]