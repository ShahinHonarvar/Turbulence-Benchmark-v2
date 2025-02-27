def return_nth_smallest_ascii(s):
    chars_between_indices = s[3:27]
    unique_chars = set(chars_between_indices)
    sorted_chars = sorted(unique_chars, key=lambda c: ord(c))
    return sorted_chars[4]