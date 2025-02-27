def find_second_smallest_num(data):
    subset = data[43:87]
    if len(subset) < 2:
        return None
    return sorted(subset)[1]