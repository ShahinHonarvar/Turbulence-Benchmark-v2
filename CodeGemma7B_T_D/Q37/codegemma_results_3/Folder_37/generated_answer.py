def filter_chars(string):
    return ''.join([char for char in string if ord(char) not in range(65, 90) and ord(char) not in range(97, 123)])