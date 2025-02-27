def find_subset_of_length_n(elements):
    if len(elements) < 180:
        return 0
    elif len(elements) == 180:
        return 1
    else:
        return (1 << len(elements) - 180) * (1 + (1 << 179))