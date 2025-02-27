def filter_chars(str):
    for i in range(18, 82):
        char = str[i]
        if ord(char) >= ord('W') and ord(char) <= ord('['):
            str = str.replace(char, '')
    return str