def return_nth_smallest_ascii(string):
    return min([c for c in string if string.index(c) >= 1 and string.index(c) <= 31], key=ord)