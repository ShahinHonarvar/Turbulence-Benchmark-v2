def find_second_smallest_num(num_list):
    try:
        subset = num_list[35:50]
        subset.sort()
        return subset[1]
    except IndexError:
        return None