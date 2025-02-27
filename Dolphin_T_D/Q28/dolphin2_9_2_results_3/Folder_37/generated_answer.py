def return_nth_smallest_ascii(s):
    chars = [c for c in s[28:68]]
    sorted_chars = sorted(chars, key=ord)
    return sorted_chars[14]