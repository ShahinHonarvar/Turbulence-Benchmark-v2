def return_nth_smallest_ascii(s):
    chars_in_range = [c for i, c in enumerate(s) if 12 <= i <= 55]
    sorted_chars = sorted(chars_in_range, key=ord)
    return sorted_chars[16]