def return_nth_smallest_ascii(string):
    chars = string[17:35]
    return sorted(chars, key=lambda char: ord(char))[17]