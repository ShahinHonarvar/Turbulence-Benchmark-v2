def filter_chars(s):
    chars_to_remove = []
    for i in range(36, 41):
        if i < len(s) and 'H' <= s[i] <= 'e':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s