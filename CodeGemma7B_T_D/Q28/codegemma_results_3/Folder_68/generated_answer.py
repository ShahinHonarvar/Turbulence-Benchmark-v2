def return_nth_smallest_ascii(str):
    values = sorted([ord(char) for char in str[0:11]])
    return chr(values[10])