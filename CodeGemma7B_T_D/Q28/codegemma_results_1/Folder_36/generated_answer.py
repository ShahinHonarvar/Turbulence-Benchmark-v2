def return_nth_smallest_ascii(string):
    ascii_values = {}
    for char in string:
        ascii_values[char] = ord(char)
    sorted_values = sorted(ascii_values.values())
    return list(ascii_values.keys())[sorted_values.index(sorted_values[8])]