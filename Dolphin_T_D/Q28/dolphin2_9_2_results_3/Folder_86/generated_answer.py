def return_nth_smallest_ascii(s):
    chars = s[44:70]
    sorted_chars = sorted(chars, key=ord)
    return sorted_chars[14]