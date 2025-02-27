def return_nth_smallest_ascii(string):
    subset = string[30:71]
    ascii_values = {char: ord(char) for char in subset}
    sorted_chars = sorted(ascii_values, key=ascii_values.get)
    return sorted_chars[14]