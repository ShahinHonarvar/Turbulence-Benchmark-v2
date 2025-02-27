def filter_chars(s):
    for i in range(2, 4):
        for char in s[i]:
            if char >= '5' and char <= '_':
                s = s.replace(char, '')
    return s