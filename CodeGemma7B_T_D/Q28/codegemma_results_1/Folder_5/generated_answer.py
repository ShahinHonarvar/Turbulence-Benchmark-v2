def return_nth_smallest_ascii(string):
    chars = sorted([c for c in string if string.index(c) in range(5, 90)])
    return chars[12]