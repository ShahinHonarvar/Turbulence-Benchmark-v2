def filter_chars(str1):
    truthy_chars = [ch for ch in str1 if ord(ch) > ord('!') and ord(ch) < ord('*')]
    return ''.join((ch for ch in str1 if ch not in truthy_chars))