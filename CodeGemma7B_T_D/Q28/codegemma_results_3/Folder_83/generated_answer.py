def return_nth_smallest_ascii(string):
    string = string[30:71]
    ascii_values = sorted(list(map(ord, string)))
    return chr(ascii_values[14])