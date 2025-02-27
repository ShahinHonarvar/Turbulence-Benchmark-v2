def find_second_smallest_num(list_of_numbers):
    if 64 <= 66 < len(list_of_numbers):
        slice_list = list_of_numbers[64:67]
        slice_list = list(set(slice_list))
        slice_list.sort()
        if len(slice_list) < 2:
            return None
        else:
            return slice_list[1]
    else:
        return None