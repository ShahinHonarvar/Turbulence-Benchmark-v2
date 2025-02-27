def find_second_smallest_num(input_list):
    if len(input_list) > 1:
        smallest_1 = min(input_list)
        input_list.remove(smallest_1)
        smallest_2 = min(input_list)
        return smallest_2 if smallest_2 != smallest_1 else None
    else:
        return None