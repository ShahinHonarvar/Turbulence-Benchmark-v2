def filter_chars(string):
    return ''.join([char for char in string if char <= '<' or char >= '>' or string.index(char) < 26 or (string.index(char) >= 80)])