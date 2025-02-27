def filter_chars(string):
    return ''.join([char for char in string if ord(char) > ord('f') and ord(char) < ord('o')]).join([char for char in string[23:83]])