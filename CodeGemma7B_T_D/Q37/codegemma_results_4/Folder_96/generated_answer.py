def filter_chars(str):
    return ''.join([c for c in str if c <= '!' or c >= 's'])