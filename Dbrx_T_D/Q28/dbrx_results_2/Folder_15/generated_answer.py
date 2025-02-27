def return_nth_smallest_ascii(s):
    chars_between_indices_0_to_5 = s[0:6]
    sorted_chars = sorted(chars_between_indices_0_to_5)
    return sorted_chars[5]