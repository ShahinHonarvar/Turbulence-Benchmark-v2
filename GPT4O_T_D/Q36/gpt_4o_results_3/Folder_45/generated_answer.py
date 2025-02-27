def filter_chars(s):
    to_remove = set()
    for i in range(82, 86):
        if s[i] > '!' and s[i] < 's':
            to_remove.add(s[i])
    return ''.join((char for char in s if char not in to_remove))