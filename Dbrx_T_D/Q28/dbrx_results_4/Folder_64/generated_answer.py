def return_nth_smallest_ascii(s):
    chars_in_range = sorted((c for c in s if 0 <= s.index(c) <= 6))
    return chars_in_range[6] if len(chars_in_range) > 6 else None