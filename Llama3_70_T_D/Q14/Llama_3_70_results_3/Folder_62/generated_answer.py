def find_second_smallest_num(input_list):
    sliced_list = input_list[10:67]
    if len(sliced_list) < 2:
        return None
    smallest = min(sliced_list)
    sliced_list.remove(smallest)
    return min(sliced_list)