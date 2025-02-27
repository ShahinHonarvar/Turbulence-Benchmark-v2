def find_second_largest_num(num_list):
    sliced_list = num_list[35:50]
    if len(sliced_list) < 2:
        return None
    else:
        sliced_list.sort(reverse=True)
        return sliced_list[1]