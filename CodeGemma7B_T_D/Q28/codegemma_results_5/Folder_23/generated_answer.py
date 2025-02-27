def return_nth_smallest_ascii(string):
    chars = sorted([char for char in string[29:48]], key=ord)
    return chars[6]