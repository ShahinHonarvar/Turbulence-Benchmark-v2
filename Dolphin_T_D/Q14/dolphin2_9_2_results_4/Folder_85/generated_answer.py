def find_second_smallest_num(num_list):
    if len(num_list) < 2:
        return None
    smallest = min(num_list[0:7])
    num_list.remove(smallest)
    if len(num_list) < 2:
        return None
    return min(num_list)