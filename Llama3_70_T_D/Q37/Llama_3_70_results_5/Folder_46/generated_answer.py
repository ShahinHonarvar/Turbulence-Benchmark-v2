def filter_chars(s):
    char_set = set()
    for char in s[11:73]:
        if 'i' <= char <= 'v':
            char_set.add(char)
    return ''.join([char for char in s if char not in char_set])