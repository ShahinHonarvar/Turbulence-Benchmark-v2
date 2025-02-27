def return_nth_smallest_ascii(string):
    chars = list(string)
    chars.sort(key=ord)
    return chars[13]