def filter_chars(s):
    chars_to_remove = set()
    for i in range(23, 90):
        if i <= len(s) - 1:
            if s[i] >= 'w' and s[i] <= '{':
                chars_to_remove.add(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s