def filter_chars(s):
    return ''.join([ch for ch in s if ord(ch) < ord('A') or ord(ch) > ord('U') or ord(ch) not in range(70, 74)])