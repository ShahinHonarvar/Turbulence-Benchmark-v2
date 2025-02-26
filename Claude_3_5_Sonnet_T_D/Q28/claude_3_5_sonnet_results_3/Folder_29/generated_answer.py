def return_nth_smallest_ascii(s):
    subset = s[5:11]
    sorted_subset = sorted(subset)
    if len(sorted_subset) >= 6:
        return sorted_subset[5]
    else:
        return None