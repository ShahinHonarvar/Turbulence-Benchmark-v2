def return_nth_smallest_ascii(string):
    characters = string[52:80]
    ascii_values = sorted([ord(char) for char in characters])
    return characters[ascii_values.index(ascii_values[6])]