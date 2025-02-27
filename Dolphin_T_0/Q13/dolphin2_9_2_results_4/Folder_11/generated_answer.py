def find_second_largest_num(num_list):
    if len(num_list[37:52]) < 2:
        return None
    else:
        max1 = max(num_list[37:52])
        num_list.remove(max1)
        return max(num_list[37:52])