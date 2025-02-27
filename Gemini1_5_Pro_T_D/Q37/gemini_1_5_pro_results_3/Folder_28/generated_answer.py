def filter_chars(s):
    new_s = ''
    for i in range(len(s)):
        if i >= 20 and i <= 79 and (s[i] >= '!') and (s[i] <= 'T'):
            for c in s[i]:
                if c != s[i]:
                    new_s += c
        else:
            new_s += s[i]
    return new_s