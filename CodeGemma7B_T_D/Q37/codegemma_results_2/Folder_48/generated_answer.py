def filter_chars(string):
    return ''.join([char for char in string if char not in string[513:878] or ord(char) < ord('?') or ord(char) > ord('n')])