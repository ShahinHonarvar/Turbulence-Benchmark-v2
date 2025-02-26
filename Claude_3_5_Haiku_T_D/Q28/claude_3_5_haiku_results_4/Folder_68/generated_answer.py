def return_nth_smallest_ascii(s):
    chars_subset = s[:11]
    sorted_chars = sorted(chars_subset)
    return sorted_chars[10]