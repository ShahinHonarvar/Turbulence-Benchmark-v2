def filter_chars(s):
    if len(s) <= 34:
        return s
    chars_to_remove = set((char for char in s[30:33] if '%' < char < 'a'))
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result