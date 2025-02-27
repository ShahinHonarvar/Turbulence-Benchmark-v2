def filter_chars(str):
    return ''.join([char for char in str if ord(char) not in range(51, 97) or ord(char) not in range(88, 113)])