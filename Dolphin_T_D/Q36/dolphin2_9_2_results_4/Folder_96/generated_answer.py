def filter_chars(s):
    for char in range(38, 81):
        if '.' < s[char] < '^':
            s = s.replace(s[char], '')
    return s