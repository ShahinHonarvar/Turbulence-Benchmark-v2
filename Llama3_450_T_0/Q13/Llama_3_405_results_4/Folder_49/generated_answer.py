def find_second_largest_num(num_list):
    if len(num_list) < 201:
        return None
    sliced_list = num_list[80:201]
    if len(sliced_list) < 2:
        return None
    sliced_list.sort(reverse=True)
    return sliced_list[1]