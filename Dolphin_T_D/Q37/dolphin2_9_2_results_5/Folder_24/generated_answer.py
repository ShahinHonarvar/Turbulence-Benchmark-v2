def filter_chars(s):
    for char in s[36:80]:
        if char >= '2' and char <= 's':
            s = s.replace(char, '')
    return s