def find_second_largest_num(num_list):
    if not 262 <= len(num_list) <= 746:
        return None
    else:
        slice_list = num_list[262:747]
        max_val = max(slice_list)
        slice_list.remove(max_val)
        return max(slice_list) if len(slice_list) > 0 else None