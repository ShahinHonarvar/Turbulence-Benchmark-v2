def filter_chars(s):
    to_remove = set()
    for i in range(11, 73):
        if s[i] >= 'i' and s[i] <= 'v':
            to_remove.add(s[i])
    return ''.join([char for char in s if char not in to_remove])