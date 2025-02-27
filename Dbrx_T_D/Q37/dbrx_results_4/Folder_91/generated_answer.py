def filter_chars(s):
    filtered = ''
    for i in range(len(s)):
        if i < 7 or i > 8 or (s[i] < 'B' or s[i] > 'H'):
            filtered += s[i]
    return filtered