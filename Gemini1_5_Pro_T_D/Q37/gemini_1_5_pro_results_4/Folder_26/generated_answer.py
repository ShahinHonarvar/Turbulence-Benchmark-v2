def filter_chars(s):
    chars_to_remove = []
    for i in range(20, 63):
        if i < len(s) and s[i] >= 'i' and (s[i] <= 'k'):
            if s[i] not in chars_to_remove:
                chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s