def return_nth_smallest_ascii(string):
    return min([char for char in string[60:89] if ord(char) <= ord('z') and ord(char) >= ord('a')], default=None)