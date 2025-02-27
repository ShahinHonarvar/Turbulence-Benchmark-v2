def find_second_largest_num(num_list):
    subset = num_list[35:50]
    if len(subset) < 2:
        return None
    else:
        values = list(set(subset))
        values.sort()
        return values[1]