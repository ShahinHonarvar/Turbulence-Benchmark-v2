def filter_chars(s):
    chars_to_remove = set(s[43:83])
    chars_to_remove = {char for char in chars_to_remove if ':' < char < 'Q'}
    return ''.join((char for char in s if char not in chars_to_remove))