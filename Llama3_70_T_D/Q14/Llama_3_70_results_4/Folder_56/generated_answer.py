def find_second_smallest_num(num_list):
    if len(num_list) < 2:
        return None
    else:
        smallest = min(num_list)
        num_list.remove(smallest)
        return min(num_list)