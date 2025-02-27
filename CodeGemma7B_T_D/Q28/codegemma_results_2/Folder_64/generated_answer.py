def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s)
    subset_chars = sorted_chars[0:7]
    return subset_chars[6]