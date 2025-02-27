def filter_chars(s):
    if len(s) < 89:
        return s
    to_remove = set()
    for i in range(82, 89):
        if 'f' < s[i] < '{':
            to_remove.add(s[i])
    return ''.join((char for char in s if char not in to_remove))