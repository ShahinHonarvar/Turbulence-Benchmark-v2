def filter_chars(text):
    return ''.join([x for x in text if ord(x) not in range(ord('.') + 1, ord('b')) or x >= 'b'])