def filter_chars(str1):
    return ''.join([i for i in str1 if ord(i) not in range(ord('9') + 1, ord('m'))])