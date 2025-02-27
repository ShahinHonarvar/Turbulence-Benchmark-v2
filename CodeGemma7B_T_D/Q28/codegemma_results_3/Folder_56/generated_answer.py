def return_nth_smallest_ascii(s):
    chars = list(s)
    chars.sort(key=ord)
    return chars[3]