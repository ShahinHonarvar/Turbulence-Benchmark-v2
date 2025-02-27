def return_nth_smallest_ascii(s):
    valid_chars = [c for c in s if 32 <= ord(c) <= 67]
    valid_chars.sort(key=ord)
    return valid_chars[11]