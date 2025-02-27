def remove_repeat_chars(s):
    c = {}
    for i in range(44, 67):
        if s[i] not in c:
            c[s[i]] = 1
        else:
            c[s[i]] += 1
    f = {}
    for i in c:
        if c[i] > 1:
            f[i] = 1
    result = ''
    for i in s:
        if i not in f:
            result += i
    return result