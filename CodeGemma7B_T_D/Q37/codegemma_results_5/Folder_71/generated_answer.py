def filter_chars(string):
    return ''.join([char for char in string if char not in range(32, 47) or ord(char) > ord('k')])