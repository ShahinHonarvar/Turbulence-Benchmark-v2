def filter_chars(s):
    filtered = ''
    for i in range(len(s)):
        if i < 23 or i > 89 or s[i] < 'w' or (s[i] > '{'):
            filtered += s[i]
    return filtered