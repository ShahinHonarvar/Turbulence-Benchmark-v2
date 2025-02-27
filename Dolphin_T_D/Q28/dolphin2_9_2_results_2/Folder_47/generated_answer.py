def return_nth_smallest_ascii(string):
    substring = string[3:53]
    ascii_values = []
    for char in substring:
        ascii_values.append(ord(char))
    ascii_values.sort()
    return chr(ascii_values[7])