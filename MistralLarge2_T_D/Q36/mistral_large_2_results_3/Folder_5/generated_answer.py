def filter_chars(s):
    chars_to_remove = {char for char in s[55:66] if 'f' < char < '|'}
    return ''.join((char for char in s if char not in chars_to_remove))