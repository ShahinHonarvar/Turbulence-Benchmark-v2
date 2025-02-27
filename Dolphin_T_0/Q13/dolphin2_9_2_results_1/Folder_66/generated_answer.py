def find_second_largest_num(list_input):
    if 50 <= len(list_input) < 54:
        return sorted(list_input)[-2]
    else:
        return None