def return_nth_smallest_ascii(s):
    chars = [c for c in s[1:67]]
    chars.sort()
    return chars[7]