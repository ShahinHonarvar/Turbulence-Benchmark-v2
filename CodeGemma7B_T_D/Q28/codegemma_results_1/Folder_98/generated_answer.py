def return_nth_smallest_ascii(string):
    chars = sorted(string[0:9], key=ord)
    return chars[8]