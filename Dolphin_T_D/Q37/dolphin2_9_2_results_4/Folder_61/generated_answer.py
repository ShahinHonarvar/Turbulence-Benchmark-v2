def filter_chars(s):
    char_set = set(s[5:7])
    result = ''
    for c in s:
        if c not in char_set or c < 'G' or c > 'p':
            result += c
    return result