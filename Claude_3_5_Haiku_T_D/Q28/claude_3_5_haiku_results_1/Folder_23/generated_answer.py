def return_nth_smallest_ascii(s):
    subset = s[29:48]
    sorted_subset = sorted(set(subset), key=lambda x: ord(x))
    return sorted_subset[6]