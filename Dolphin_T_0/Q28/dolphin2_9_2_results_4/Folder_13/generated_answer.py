def return_nth_smallest_ascii(s):
    chars = [c for c in s if 47 <= ord(c) <= 80]
    chars.sort(key=ord)
    return chars[3]