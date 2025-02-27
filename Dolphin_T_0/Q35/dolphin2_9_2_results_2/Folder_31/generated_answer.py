def remove_repeat_chars(s):
    count = {}
    for i in range(33, 78):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    for char, n in count.items():
        if n > 1:
            s = s.replace(char, '')
    return s