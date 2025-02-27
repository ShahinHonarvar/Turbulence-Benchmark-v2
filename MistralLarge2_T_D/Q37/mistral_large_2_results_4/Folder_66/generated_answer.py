def filter_chars(s):
    chars_to_remove = set(s[27:86]) & set('cdefghi')
    return ''.join((char for char in s if char not in chars_to_remove))