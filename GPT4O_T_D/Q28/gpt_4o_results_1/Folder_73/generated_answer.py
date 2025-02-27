def return_nth_smallest_ascii(s):
    subset = sorted(s[:70])
    if len(subset) < 10:
        return None
    return subset[9]