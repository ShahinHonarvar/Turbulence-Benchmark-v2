def return_nth_smallest_ascii(s):
    chars = s[5:48]
    sorted_chars = sorted(chars, key=ord)
    return sorted_chars[12]