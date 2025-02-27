def return_nth_smallest_ascii(s):
    chars_between_indices = s[1:67]
    unique_chars = sorted(set(chars_between_indices))
    return unique_chars[7]