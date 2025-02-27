def return_nth_smallest_ascii(s):
    characters = list(s[14:55])
    ascii_values = [ord(c) for c in characters]
    ascii_values.sort()
    return characters[ascii_values.index(ascii_values[10])]