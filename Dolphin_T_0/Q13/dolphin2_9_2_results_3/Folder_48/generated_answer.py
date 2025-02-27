def find_second_largest_num(num_list):
    if 533 <= len(num_list) <= 605:
        num_slice = num_list[533:606]
        if len(num_slice) > 1:
            max_num = max(num_slice)
            num_slice.remove(max_num)
            if len(num_slice) > 0:
                return max(num_slice)
            else:
                return None
        else:
            return None
    else:
        return None