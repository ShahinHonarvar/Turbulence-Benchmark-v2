def filter_chars(str1):
    str1 = ''.join([char for char in str1 if not (20 < ord(char) <= 89 and ord(char) >= ord('F') <= ord('h'))])
    return str1