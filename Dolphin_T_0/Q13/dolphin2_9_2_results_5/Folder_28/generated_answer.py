def find_second_largest_num(num_list):
    center_slice = num_list[62:64]
    if len(center_slice) != 2:
        return None
    else:
        sorted_slice = sorted(center_slice)
        if sorted_slice[1] == sorted_slice[-1]:
            return None
        else:
            return sorted_slice[1]