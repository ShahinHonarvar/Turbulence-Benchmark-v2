def filter_chars(s):
    chars_to_remove = set()
    for char in s[41:63]:
        if '7' < char < 'H':
            chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))