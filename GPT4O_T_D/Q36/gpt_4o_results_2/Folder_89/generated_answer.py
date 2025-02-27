def filter_chars(s):
    remove_chars = set()
    filtered_range = s[58:69]
    for char in filtered_range:
        if '(' < char < 'W':
            remove_chars.add(char)
    result = ''.join((char for char in s if char not in remove_chars))
    return result