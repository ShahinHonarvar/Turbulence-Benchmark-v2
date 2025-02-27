def return_nth_smallest_ascii(s):
    chars = [c for c in s if 34 <= ord(c) <= 68]
    chars.sort(key=ord)
    return chars[5]