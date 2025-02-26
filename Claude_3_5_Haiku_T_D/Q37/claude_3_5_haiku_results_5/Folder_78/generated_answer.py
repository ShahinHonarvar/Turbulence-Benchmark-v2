def filter_chars(s):
    chars_to_remove = set((char for char in s[75:100] if '8' <= char <= 'e'))
    return ''.join((char for char in s if char not in chars_to_remove))