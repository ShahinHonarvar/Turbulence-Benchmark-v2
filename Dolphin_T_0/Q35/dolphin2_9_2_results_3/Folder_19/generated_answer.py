def remove_repeat_chars(s):
    count = {}
    for i in range(1, 4):
        if s[i] in count:
            del count[s[i]]
        else:
            count[s[i]] = 1
    for key in count:
        s = s.replace(key, '')
    return s