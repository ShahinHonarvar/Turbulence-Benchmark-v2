def filter_chars(s):
    chars_to_remove = {char for char in s[23:45] if '3' < char < 'I'}
    return ''.join((char for char in s if char not in chars_to_remove))