def filter_chars(s):
    target_range = [char for char in s[75:100] if '8' <= char <= 'e']
    return ''.join((char for char in s if char not in target_range))