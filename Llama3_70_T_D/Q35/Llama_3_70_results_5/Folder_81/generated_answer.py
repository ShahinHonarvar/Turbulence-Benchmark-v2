def remove_repeat_chars(s):
    count = {}
    for i in range(20, 200):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    for char in [c for c, v in count.items() if v > 1]:
        s = s.replace(char, '')
    return s