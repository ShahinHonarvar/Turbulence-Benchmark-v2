def return_nth_smallest_ascii(s):
    if len(s) < 27:
        return None
    subset = s[8:27]
    sorted_subset = sorted(subset)
    return sorted_subset[5]