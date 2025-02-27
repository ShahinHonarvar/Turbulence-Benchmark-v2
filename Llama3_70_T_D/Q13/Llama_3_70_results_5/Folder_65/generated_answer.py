def find_second_largest_num(num_list):
    sliced_list = num_list[56:99]
    if len(sliced_list) < 2:
        return None
    sliced_list.sort(reverse=True)
    return sliced_list[1]