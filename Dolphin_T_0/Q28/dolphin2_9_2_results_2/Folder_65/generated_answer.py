def return_nth_smallest_ascii(s):
    chars = [c for c in s if 32 <= ord(c) <= 67]
    chars.sort(key=ord)
    return chars[11]