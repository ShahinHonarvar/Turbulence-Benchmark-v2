def filter_chars(s):
    chars_to_remove = {s[i] for i in range(4, 5) if '7' <= s[i] <= 'o'}
    return ''.join([char for char in s if char not in chars_to_remove])