def filter_chars(s):
    chars_to_remove = {char for char in s[66:90] if '#' < char < 'T'}
    return ''.join((char for char in s if char not in chars_to_remove))