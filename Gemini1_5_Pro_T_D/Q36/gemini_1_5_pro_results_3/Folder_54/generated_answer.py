def filter_chars(s):
    chars_to_remove = []
    for i in range(19, 38):
        if i < len(s) and ord(s[i]) > ord(')') and (ord(s[i]) < ord('P')):
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s