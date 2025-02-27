def filter_chars(s):
    new_s = ''
    for i in range(len(s)):
        if i < 36 or i > 40 or (s[i] < 'H' or s[i] > 'e'):
            new_s += s[i]
    return new_s