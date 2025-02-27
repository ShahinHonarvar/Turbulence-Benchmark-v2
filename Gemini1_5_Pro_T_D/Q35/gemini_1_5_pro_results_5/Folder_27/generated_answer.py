def remove_repeat_chars(s):
    repeats = []
    for i in range(87, 89):
        if s.count(s[i]) > 1 and s[i] not in repeats:
            repeats.append(s[i])
    for char in repeats:
        s = s.replace(char, '')
    return s