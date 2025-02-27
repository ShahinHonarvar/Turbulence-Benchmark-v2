def filter_chars(s):
    for i in range(73, 75):
        for char in s:
            if char.index(char) in range(73, 75):
                if char >= 'U' and char <= 'l':
                    s = s.replace(char, '')
    return s