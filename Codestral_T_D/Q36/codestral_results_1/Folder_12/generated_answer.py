def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(32, 85) if 'm' < chr(i) < 'w']
    return ''.join([char for char in s if char not in chars_to_remove])