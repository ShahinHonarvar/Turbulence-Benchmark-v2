def filter_chars(s):
    chars = [s[i] for i in range(3, 9) if '*' < s[i] < 'E']
    for c in chars:
        while c in s:
            s = s.replace(c, '', 1)
    return s