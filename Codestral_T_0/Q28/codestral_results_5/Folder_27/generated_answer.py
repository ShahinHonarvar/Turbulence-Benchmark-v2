def return_nth_smallest_ascii(s):
    valid_chars = [c for c in s if 33 <= ord(c) <= 85]
    valid_chars.sort(key=ord)
    return valid_chars[12]