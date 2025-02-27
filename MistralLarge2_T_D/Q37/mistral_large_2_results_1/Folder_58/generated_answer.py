def filter_chars(s):
    chars_to_remove = {s[i] for i in range(503, 754) if '9' <= s[i] <= 'w'}
    return ''.join((char for char in s if char not in chars_to_remove))