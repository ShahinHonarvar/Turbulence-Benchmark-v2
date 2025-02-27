def return_nth_smallest_ascii(s):
    chars_between_indices = s[37:60]
    sorted_chars = sorted(chars_between_indices, key=lambda x: ord(x))
    return sorted_chars[5]