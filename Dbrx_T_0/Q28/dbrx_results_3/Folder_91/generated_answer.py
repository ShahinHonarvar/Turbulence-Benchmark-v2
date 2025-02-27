def return_nth_smallest_ascii(s):
    chars_in_range = [c for c in s if 0 <= ord(c) - ord(s[0]) <= 7]
    sorted_chars = sorted(chars_in_range)
    return sorted_chars[7] if len(sorted_chars) > 7 else None