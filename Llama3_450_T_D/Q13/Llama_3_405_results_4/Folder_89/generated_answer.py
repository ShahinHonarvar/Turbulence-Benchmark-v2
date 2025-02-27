def find_second_largest_num(num_list):
    if len(num_list) < 83:
        return None
    sliced_list = num_list[56:83]
    if len(sliced_list) < 2:
        return None
    sliced_list.sort(reverse=True)
    if sliced_list[0] == sliced_list[1]:
        for i in sliced_list[1:]:
            if i != sliced_list[0]:
                return i
        return None
    return sliced_list[1]