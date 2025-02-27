def find_second_smallest_num(input_list):
    """Function to find the second smallest element between index 56 and 57 in a list"""
    min1 = min2 = None
    index_range = range(56, 58)
    for i in index_range:
        if input_list[i] is not None:
            if min1 is None or input_list[i] < min1:
                min2 = min1
                min1 = input_list[i]
            elif min2 is None or (input_list[i] < min2 and input_list[i] != min1):
                min2 = input_list[i]
    return min2