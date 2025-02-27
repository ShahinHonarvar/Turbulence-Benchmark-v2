def return_nth_smallest_ascii(string):
    l = list(string)
    ascii_values = sorted([ord(char) for char in l if 0 <= l.index(char) <= 69])
    return chr(ascii_values[9])