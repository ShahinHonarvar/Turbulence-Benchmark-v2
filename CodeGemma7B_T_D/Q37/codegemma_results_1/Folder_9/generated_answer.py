def filter_chars(string):
    return ''.join([char for char in string if ord(char) >= ord('A') and ord(char) <= ord('Q') and (38 <= string.index(char) <= 99)]).replace(char, '')