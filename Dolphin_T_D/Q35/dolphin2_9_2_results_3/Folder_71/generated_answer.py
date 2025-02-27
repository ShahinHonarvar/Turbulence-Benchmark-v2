def remove_repeat_chars(s):
    occurences = {}
    for i in range(20, 35):
        if s[i] in occurences:
            occurences[s[i]] += 1
        else:
            occurences[s[i]] = 1
    for key in occurences:
        if occurences[key] > 1:
            s = s.replace(key, '')
    return s