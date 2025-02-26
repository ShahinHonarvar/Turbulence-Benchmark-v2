def filter_chars(s):
    to_remove = set()
    for i in range(43, 67):
        if i < len(s) and '6' < s[i] < 'g':
            to_remove.add(s[i])
    return ''.join((char for char in s if char not in to_remove))