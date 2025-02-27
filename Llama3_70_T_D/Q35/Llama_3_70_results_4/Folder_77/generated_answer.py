def remove_repeat_chars(s):
    count = {}
    for i in range(355, 988):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    r = ''
    for c in s:
        if c not in count or count[c] == 1:
            r += c
    return r