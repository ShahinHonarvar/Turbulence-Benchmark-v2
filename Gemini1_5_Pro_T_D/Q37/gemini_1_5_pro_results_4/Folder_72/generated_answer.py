def filter_chars(s):
    chars_to_remove = []
    for i in range(35, 52):
        if i < len(s) and 'H' <= s[i] <= 's':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s