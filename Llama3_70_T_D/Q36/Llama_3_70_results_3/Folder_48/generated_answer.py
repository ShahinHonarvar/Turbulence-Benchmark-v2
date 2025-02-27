def filter_chars(s):
    chars_to_remove = set(s[154:222])
    chars_to_remove = {char for char in chars_to_remove if 'A' < char < 'f'}
    return ''.join([char for char in s if char not in chars_to_remove])