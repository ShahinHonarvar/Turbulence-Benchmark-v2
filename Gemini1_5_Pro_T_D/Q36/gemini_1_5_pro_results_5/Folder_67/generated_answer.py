def filter_chars(s):
    chars_to_remove = []
    for i in range(19, 30):
        if s[i] > 'H' and s[i] < '|':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s