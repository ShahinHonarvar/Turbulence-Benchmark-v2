def return_nth_smallest_ascii(s):
    subset = s[6:59]
    sorted_subset = sorted(subset, key=lambda x: ord(x))
    return sorted_subset[18]