def find_second_smallest_num(input_list):
    sliced_list = input_list[59:98]
    if len(sliced_list) < 2:
        return None
    smallest = min(sliced_list)
    sliced_list.remove(smallest)
    return min(sliced_list)