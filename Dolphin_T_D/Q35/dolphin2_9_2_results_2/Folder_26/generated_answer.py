def remove_repeat_chars(s):
    count = {}
    for i in range(68, 99):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    for char, value in count.items():
        if value > 1:
            s = s.replace(char, '')
    return s