def return_nth_smallest_ascii(s):
    subset = s[12:73]
    sorted_subset = sorted(subset, key=lambda x: ord(x))
    return sorted_subset[12]