def filter_chars(s):
    new_str = ''
    for i in range(len(s)):
        if s[i] in s[82:93] and s[i] != '*' and (s[i] != '!'):
            continue
        new_str += s[i]
    return new_str