def filter_chars(text):
    return ''.join([char for char in text if not (42 <= ord(char) <= 92 and ord(char) > ord('/') and (ord(char) < ord('a')))])