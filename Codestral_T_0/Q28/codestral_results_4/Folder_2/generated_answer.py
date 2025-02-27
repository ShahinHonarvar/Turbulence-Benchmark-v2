def return_nth_smallest_ascii(s):
    valid_chars = [c for c in s if 48 <= ord(c) <= 76]
    valid_chars.sort(key=ord)
    return valid_chars[4]