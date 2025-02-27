def find_second_largest_num(num_list):
    if len(num_list) == 0:
        return None
    elif len(num_list) == 1:
        return None
    else:
        second_largest_num_index_29_51 = None
        for i in range(29, 52):
            if num_list[i] != max(num_list[29:52]) and second_largest_num_index_29_51 is None:
                second_largest_num_index_29_51 = num_list[i]
            elif num_list[i] > second_largest_num_index_29_51 and num_list[i] != max(num_list[29:52]):
                second_largest_num_index_29_51 = num_list[i]
        if second_largest_num_index_29_51 is None:
            return None
        else:
            return second_largest_num_index_29_51