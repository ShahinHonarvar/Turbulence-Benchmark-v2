def remove_repeat_chars(s):
    c = []
    p = []
    for i in range(8):
        if s[i] not in c:
            c.append(s[i])
        elif s[i] not in p:
            p.append(s[i])
    return ''.join([ch for ch in s if ch not in p])