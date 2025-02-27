def filter_chars(s):
    for i in range(13, 40):
        if ':' < s[i] < 'C':
            s = ''.join((char for char in s if char != s[i]))
    return s