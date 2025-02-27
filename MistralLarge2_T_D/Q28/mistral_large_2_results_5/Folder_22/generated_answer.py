def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[:17], key=ord)
    return sorted_chars[16]