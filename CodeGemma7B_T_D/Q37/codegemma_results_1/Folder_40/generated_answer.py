def filter_chars(txt):
    return ''.join([char for char in txt if ord(char) > ord('*') and ord(char) <= ord('s')]).replace(txt, '')