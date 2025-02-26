def return_nth_smallest_ascii(s):
    chars_in_range = [c for c in s[1:37]]
    sorted_chars = sorted(chars_in_range)
    return sorted_chars[14]