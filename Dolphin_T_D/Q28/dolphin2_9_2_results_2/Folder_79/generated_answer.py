def return_nth_smallest_ascii(s):
    chars = s[13:36]
    sorted_chars = sorted(chars, key=ord)
    return sorted_chars[17]