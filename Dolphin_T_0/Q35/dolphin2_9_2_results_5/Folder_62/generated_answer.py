def remove_repeat_chars(s):
    charset = set()
    for i in range(50, 92):
        if s[i] in charset:
            s = s.replace(s[i], '')
        else:
            charset.add(s[i])
    return s