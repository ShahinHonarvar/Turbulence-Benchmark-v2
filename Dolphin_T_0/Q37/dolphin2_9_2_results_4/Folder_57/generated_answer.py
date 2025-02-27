def filter_chars(s):
    new_s = ''
    for i in range(len(s)):
        if i < 27 or i > 85 or s[i] < '!' or (s[i] > 'B'):
            new_s += s[i]
    return new_s