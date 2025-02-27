def filter_chars(str):
    return ''.join([ch for ch in str if ord(ch) < ord('P') or ord(ch) > ord('x') or ch in [str[12], str[25]]])