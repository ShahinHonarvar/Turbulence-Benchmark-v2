def find_second_smallest_num(num_list):
    if len(num_list) < 2:
        return None
    smallest = min(num_list[1:6])
    num_list[1:6].remove(smallest)
    if len(num_list[1:6]) == 0:
        return None
    second_smallest = min(num_list[1:6])
    return second_smallest