def find_second_largest_num(num_list):
    sliced_list = num_list[37:77]
    if len(sliced_list) < 2:
        return None
    sliced_list.remove(max(sliced_list))
    return max(sliced_list) if sliced_list else None