def filter_chars(str):
    for char in str[225:382]:
        if char.isalpha() and ord(char) >= ord('D') and (ord(char) <= ord('Y')):
            str = str.replace(char, '')
    return str