def filter_chars(s):
    char_set = set()
    for i in range(42, 78):
        if '!' < s[i] < '?':
            char_set.add(s[i])
    for char in char_set:
        s = s.replace(char, '')
    return s