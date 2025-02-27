def filter_chars(str1):
    newList = [c for c in str1 if c not in ('+', 'l')]
    return ''.join(newList)