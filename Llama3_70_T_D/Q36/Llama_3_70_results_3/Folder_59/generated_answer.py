def filter_chars(s):
    chars_to_remove = []
    for char in s[3:8]:
        if '?' < char < 'k':
            chars_to_remove.append(char)
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s