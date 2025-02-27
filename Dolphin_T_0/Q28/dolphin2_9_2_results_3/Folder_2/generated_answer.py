def return_nth_smallest_ascii(s):
    chars = [c for c in s if 48 <= ord(c) <= 76]
    chars.sort(key=ord)
    return chars[4]