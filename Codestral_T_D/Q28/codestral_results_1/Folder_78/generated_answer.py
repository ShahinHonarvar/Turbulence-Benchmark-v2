def return_nth_smallest_ascii(chars):
    chars_subset = chars[:88]
    sorted_chars = sorted(chars_subset, key=ord)
    return sorted_chars[13]