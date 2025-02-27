def find_second_largest_num(num_list):
    slicedList = num_list[10:67]
    if len(slicedList) < 2:
        return None
    return sorted(slicedList)[-2]