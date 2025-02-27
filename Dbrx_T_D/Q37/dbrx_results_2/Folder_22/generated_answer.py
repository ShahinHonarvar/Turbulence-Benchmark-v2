def filter_chars(s):
    chars_to_remove = []
    for i in range(len(s)):
        if 33 <= i <= 70:
            char = s[i]
            if '7' <= char <= 'k':
                chars_to_remove.append(char)
    for char in chars_to_remove:
        s = s.replace(char, '', 1)
    return s