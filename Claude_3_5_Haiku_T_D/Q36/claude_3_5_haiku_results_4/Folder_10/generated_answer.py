def filter_chars(s):
    to_remove = set((char for char in s[36:60] if '!' < char < 'B'))
    return ''.join((char for char in s if char not in to_remove))