def filter_chars(string):
    return ''.join([char for char in string if (ord(char) > ord('*') and ord(char) < ord('w')) == False])