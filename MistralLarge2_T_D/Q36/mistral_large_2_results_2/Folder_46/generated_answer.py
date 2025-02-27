def filter_chars(s):
    to_remove = set((char for char in s[19:69] if '<' < char < 'C'))
    return ''.join((char for char in s if char not in to_remove))