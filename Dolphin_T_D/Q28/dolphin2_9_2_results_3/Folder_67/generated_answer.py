def return_nth_smallest_ascii(string):
    characters = [string[i] for i in range(60, 84)]
    ascii_values = sorted([ord(char) for char in characters])
    return characters[ascii_values.index(ascii_values[13])]