def return_nth_smallest_ascii(s):
    unique_chars = sorted(set(s[:70]))
    return unique_chars[9]