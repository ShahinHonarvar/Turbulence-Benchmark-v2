def find_second_largest_num(num_list):
    specific_range = num_list[56:99]
    if len(specific_range) < 2:
        return None
    specific_range.sort()
    return specific_range[-2]