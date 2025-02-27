def remove_repeat_chars(s):
    count = {}
    for i in range(50, 200):
        if i < len(s):
            count[s[i]] = count.get(s[i], 0) + 1
    for c in count:
        if count[c] > 1:
            s = s.replace(c, '')
    return s