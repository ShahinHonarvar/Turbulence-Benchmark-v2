def filter_chars(s):
    chars_to_remove = {s[i] for i in range(61, 88) if '%' < s[i] < 'q'}
    return ''.join((char for char in s if char not in chars_to_remove))