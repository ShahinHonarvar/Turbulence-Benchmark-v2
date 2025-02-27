def filter_chars(s):
    chars_to_remove = {char for char in s[78:81] if 'S' < char < '['}
    return ''.join((char for char in s if char not in chars_to_remove))