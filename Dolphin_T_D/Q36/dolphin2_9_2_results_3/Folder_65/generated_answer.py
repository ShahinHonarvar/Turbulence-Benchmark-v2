def filter_chars(s):
    for char in range(58, 82):
        if 'F' < s[char] < 'O':
            while s[char] in s:
                s = s.replace(s[char], '')
    return s