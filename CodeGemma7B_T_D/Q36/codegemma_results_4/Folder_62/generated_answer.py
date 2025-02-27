def filter_chars(str):
    return ''.join([ch for ch in str if ord(ch) > ord('*') and ord(ch) < ord('w') and (ch not in str[63:89])])