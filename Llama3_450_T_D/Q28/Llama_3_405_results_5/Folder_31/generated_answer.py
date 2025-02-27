def return_nth_smallest_ascii(s):
    chars_between_indices = s[10:83]
    sorted_chars = sorted(chars_between_indices, key=lambda c: ord(c))
    return sorted_chars[17]