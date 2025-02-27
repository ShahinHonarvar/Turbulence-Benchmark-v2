def find_second_largest_num(input_list):
    subset_list = input_list[74:96]
    if len(set(subset_list)) == 1 or len(set(subset_list)) == 0:
        return None
    first = max(subset_list)
    subset_list.remove(first)
    second = max(subset_list)
    return second