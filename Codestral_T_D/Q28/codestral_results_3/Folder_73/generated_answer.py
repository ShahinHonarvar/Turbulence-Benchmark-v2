def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[:70], key=ord)
    return sorted_chars[9] if len(sorted_chars) > 9 else None