def filter_chars(s):
    return ''.join([i for i in s if ord(i) > ord('c') and ord(i) < ord('n') or i not in s[13:28]])