def filter_chars(s):
    chars_to_remove = {s[i] for i in range(81, 86) if '!' < s[i] < 's'}
    return ''.join([char for char in s if char not in chars_to_remove])