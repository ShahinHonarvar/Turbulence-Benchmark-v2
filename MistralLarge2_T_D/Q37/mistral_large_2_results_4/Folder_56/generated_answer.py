def filter_chars(s):
    to_remove = set()
    for i in range(71, 95):
        if 'K' <= s[i] <= 'a':
            to_remove.add(s[i])
    return ''.join((char for char in s if char not in to_remove))