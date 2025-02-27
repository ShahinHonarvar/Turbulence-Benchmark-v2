def return_nth_smallest_ascii(s):
    subset = s[34:86]
    sorted_subset = sorted(subset, key=lambda c: ord(c))
    return sorted_subset[19]