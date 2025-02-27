def return_nth_smallest_ascii(s):
    chars_47_to_70 = s[47:71]
    sorted_ascii_chars = sorted(chars_47_to_70)
    return sorted_ascii_chars[13]