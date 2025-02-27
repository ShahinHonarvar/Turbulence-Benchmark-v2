def filter_chars(string):
    return ''.join([char for char in string if not (51 <= ord(char) <= 96 and ord(char) >= ord('X') and (ord(char) <= ord('p')))])