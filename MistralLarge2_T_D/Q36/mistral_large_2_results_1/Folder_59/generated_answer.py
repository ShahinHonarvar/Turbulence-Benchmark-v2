def filter_chars(s):
    chars_to_remove = {char for char in s[3:8] if '?' < char < 'k'}
    return ''.join((char for char in s if char not in chars_to_remove))