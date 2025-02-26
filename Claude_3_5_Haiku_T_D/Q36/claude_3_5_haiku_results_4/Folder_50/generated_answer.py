def filter_chars(s):
    remove_chars = []
    for i in range(62, 88):
        if '%' < s[i] < 'q':
            remove_chars.append(s[i])
    for char in remove_chars:
        s = s.replace(char, '')
    return s