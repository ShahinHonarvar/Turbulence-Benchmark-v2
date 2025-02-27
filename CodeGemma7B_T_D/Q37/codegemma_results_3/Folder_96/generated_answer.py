def filter_chars(str_in):
    return ''.join([char for char in str_in if ord(char) in range(ord('!'), ord('s') + 1) and (ord(char) == ord('!') or not str_in[86:93].count(char))])