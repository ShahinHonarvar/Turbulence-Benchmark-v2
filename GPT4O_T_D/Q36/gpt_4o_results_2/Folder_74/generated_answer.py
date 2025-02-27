def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(34, 36) if '>' < chr(i) < 'A'}
    return ''.join((char for char in s if char not in chars_to_remove))