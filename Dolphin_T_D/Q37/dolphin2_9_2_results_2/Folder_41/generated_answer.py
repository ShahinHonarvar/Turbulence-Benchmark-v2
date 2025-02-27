def filter_chars(s):
    new_s = ''
    for i in range(len(s)):
        if i < 26 or i > 64 or s[i] < 'V' or (s[i] > 'o'):
            new_s += s[i]
    return new_s