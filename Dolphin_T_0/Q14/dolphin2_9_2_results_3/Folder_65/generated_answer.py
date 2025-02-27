def find_second_smallest_num(input_list):
    try:
        return sorted(input_list[56:58])[1]
    except IndexError:
        return None