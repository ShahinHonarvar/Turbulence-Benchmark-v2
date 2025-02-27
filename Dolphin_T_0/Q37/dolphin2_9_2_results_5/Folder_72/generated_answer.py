def filter_chars(s):
    s1 = []
    for i in range(len(s)):
        if i > 34 and i < 52 and (s[i] >= 'H') and (s[i] <= 's'):
            s1.append(s[i])
    s2 = [i for i in s if i not in s1]
    return ''.join(s2)