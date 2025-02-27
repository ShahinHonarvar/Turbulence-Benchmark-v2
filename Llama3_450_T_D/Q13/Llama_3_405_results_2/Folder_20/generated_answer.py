def find_second_largest_num(num_list):
    specific_range = num_list[56:67]
    if len(specific_range) < 2:
        return None
    else:
        specific_range.sort(reverse=True)
        return specific_range[1]