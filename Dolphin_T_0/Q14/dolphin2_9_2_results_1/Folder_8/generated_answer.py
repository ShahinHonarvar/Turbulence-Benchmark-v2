def find_second_smallest_num(num_list):
    num_list = num_list[56:67]
    if len(num_list) < 2:
        return None
    smallest = min(num_list)
    num_list.remove(smallest)
    second_smallest = min(num_list)
    return second_smallest