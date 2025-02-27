def return_nth_smallest_ascii(s):
    substring = s[28:68]
    sorted_chars = sorted(substring)
    sorted_chars_by_ascii = sorted(sorted_chars, key=lambda x: ord(x))
    return sorted_chars_by_ascii[14]