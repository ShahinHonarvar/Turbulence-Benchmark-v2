def filter_chars(str):
    return ''.join([char for char in str if not (38 <= ord(char) <= 99 and ord(char) >= ord('A') and (ord(char) <= ord('Q')))])