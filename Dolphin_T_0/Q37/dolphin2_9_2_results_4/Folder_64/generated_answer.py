def filter_chars(s):
    for char in s:
        if s.index(char) >= 1 and s.index(char) <= 7 and (ord(char) >= ord('L')) and (ord(char) <= ord('a')):
            s = s.replace(char, '')
    return s