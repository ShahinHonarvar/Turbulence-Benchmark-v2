def filter_chars(s):
    chars1 = []
    chars2 = []
    for char in s:
        if 11 <= s.index(char) < 46 and '!' < char < 'A':
            chars1.append(char)
        elif 11 <= s.index(char) < 46:
            chars2.append(char)
    for char in chars1:
        s = s.replace(char, '')
    for char in chars2:
        s = s.replace(char, '')
    return s