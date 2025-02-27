def remove_repeat_chars(s):
    d = {}
    for i in range(20, 35):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    result = ''
    for c in s[:20] + s[35:]:
        if c not in d:
            result += c
    for c in s[20:35]:
        if d[c] == 1:
            result += c
    return result