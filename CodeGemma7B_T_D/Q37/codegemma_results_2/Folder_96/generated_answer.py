def filter_chars(text):
    return ''.join([char for char in text if (86 <= text.index(char) <= 92 and char >= '!' and (char <= 's')) is False])