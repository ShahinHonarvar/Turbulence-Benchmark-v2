def return_nth_smallest_ascii(string):
    chars_list = string[0:8]
    chars_ascii = sorted([ord(char) for char in chars_list])
    return chr(chars_ascii[7])