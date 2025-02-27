def return_nth_smallest_ascii(s):
    chars = sorted((c for c in s[51:79]), key=ord)
    return chars[8]