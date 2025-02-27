def return_nth_smallest_ascii(string):
    if len(string) != len(set(string)):
        return None
    ascii_values = sorted([ord(char) for char in string[0:5]])
    return chr(ascii_values[4])