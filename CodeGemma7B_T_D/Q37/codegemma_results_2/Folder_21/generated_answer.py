def filter_chars(str):
    return ''.join([char for char in str if not (603 <= ord(char) <= 759 and ord(char) >= ord('Q') and (ord(char) <= ord('h')))])