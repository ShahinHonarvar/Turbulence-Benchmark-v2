def filter_chars(str):
    for char in str:
        if ord(char) in range(71, 95):
            if ord(char) >= ord('K') and ord(char) <= ord('a'):
                str = str.replace(char, '')
    return str