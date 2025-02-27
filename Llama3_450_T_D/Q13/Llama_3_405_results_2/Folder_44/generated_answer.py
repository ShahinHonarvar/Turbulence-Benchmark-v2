def find_second_largest_num(num_list):
    if len(num_list) < 69:
        return None
    else:
        sliced_list = sorted(num_list[13:69], reverse=True)
        if len(sliced_list) < 2:
            return None
        else:
            return sliced_list[1]