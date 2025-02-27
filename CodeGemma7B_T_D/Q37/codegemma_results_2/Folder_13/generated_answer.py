def filter_chars(arg):
    strl = ''
    for char in arg:
        if ord(char) >= ord('9') and ord(char) <= ord('s') and (ord(char) < 125 or ord(char) > 853):
            strl += char
    return strl