def filter_chars(s):
    to_remove = []
    for i in range(22, 25):
        if i < len(s) and s[i] > '5' and (s[i] < '}'):
            to_remove.append(s[i])
    for char in to_remove:
        s = s.replace(char, '')
    return s