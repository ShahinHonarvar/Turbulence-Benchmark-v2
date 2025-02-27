def filter_chars(s):
    if len(s) <= 19:
        return s
    chars_to_remove = set()
    for char in s[20:69]:
        if '<' < char < 'C':
            chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))