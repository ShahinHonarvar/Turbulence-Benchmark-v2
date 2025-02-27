def filter_chars(word):
    filtered_str = ''.join([char for char in word if ord(char) not in range(70, 98) or not (ord(char) > ord('V') and ord(char) < ord('j'))])
    return filtered_str