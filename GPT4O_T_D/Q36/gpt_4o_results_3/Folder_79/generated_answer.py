def filter_chars(s):
    new_str = ''
    for i in range(len(s)):
        if 11 < i < 46 and '!' < s[i] < 'A':
            new_str = s.replace(s[i], '')
        else:
            new_str = s
    return new_str