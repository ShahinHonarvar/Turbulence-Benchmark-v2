def filter_chars(s):
    return ''.join(list(filter(lambda x: not (71 <= ord(x) <= 96 and ord('_') <= ord(x) <= ord('o')), s)))