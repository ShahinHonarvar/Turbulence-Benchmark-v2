def filter_chars(s):
    result = list(s)
    to_remove = set()
    for i in range(15, 75):
        if i < len(s) and '9' < s[i] < 'K':
            to_remove.add(s[i])
    return ''.join((char for char in result if char not in to_remove))