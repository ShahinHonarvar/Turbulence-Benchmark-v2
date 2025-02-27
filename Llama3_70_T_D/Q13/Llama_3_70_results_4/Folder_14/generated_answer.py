def find_second_largest_num(num_list):
    if len(num_list) < 8:
        return None
    second_largest = sorted(num_list[5:8])[1]
    return second_largest