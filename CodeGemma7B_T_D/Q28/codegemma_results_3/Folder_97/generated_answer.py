def return_nth_smallest_ascii(string):
    subset = sorted(set([char for char in string[15:22] if char in string]))
    return subset[5] if subset else None