def return_nth_smallest_ascii(s):
    unique_chars = set(s[:10])
    sorted_chars = sorted(unique_chars, key=ord)
    return sorted_chars[9]