def return_nth_smallest_ascii(s):
    valid_chars = [ch for ch in s if 48 <= ord(ch) <= 76]
    valid_chars.sort(key=ord)
    return valid_chars[4]