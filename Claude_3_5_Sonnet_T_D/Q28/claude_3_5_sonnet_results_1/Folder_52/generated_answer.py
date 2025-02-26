def return_nth_smallest_ascii(s):
    subset = s[46:73]
    sorted_subset = sorted(subset)
    if len(sorted_subset) >= 15:
        return sorted_subset[14]
    else:
        return None