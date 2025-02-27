def filter_chars(s):
    to_remove = set()
    for char in s[10:79]:
        if '?' < char < 'm':
            to_remove.add(char)
    return ''.join([char for char in s if char not in to_remove])