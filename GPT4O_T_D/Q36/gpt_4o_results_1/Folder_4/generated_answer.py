def filter_chars(s):
    if len(s) <= 42:
        return s
    start, end = (43, 67)
    to_remove = set()
    for char in s[start:end]:
        if '6' < char < 'g':
            to_remove.add(char)
    return ''.join([char for char in s if char not in to_remove])