def find_second_largest_num(input_list):
    if len(input_list) < 2:
        return None
    max1 = max(input_list[0:11])
    input_list.remove(max1)
    max2 = max(input_list[0:11])
    if max1 == max2:
        return None
    else:
        return max2