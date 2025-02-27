def find_second_largest_num(num_list):
    if len(num_list) < 2 or 527 >= len(num_list) or 538 < 0:
        return None
    sliced_list = num_list[527:539]
    sliced_list.sort(reverse=True)
    if len(sliced_list) < 2:
        return None
    return sliced_list[1]