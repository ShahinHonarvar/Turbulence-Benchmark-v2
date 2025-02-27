def return_nth_smallest_ascii(s):
    chars = list(s[62:84])
    chars.sort(key=ord)
    return chars[8]