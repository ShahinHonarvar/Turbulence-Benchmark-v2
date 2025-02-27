def return_nth_smallest_ascii(s):
    section = s[1:32]
    sorted_chars = sorted(section)
    sorted_chars_by_ascii = sorted(sorted_chars, key=lambda x: ord(x))
    return sorted_chars_by_ascii[5]