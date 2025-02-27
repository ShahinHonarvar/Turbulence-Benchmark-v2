def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[:14], key=ord)
    return sorted_chars[13]