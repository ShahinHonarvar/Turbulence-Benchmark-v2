def remove_repeat_chars(s):
    repeats = set()
    for i in range(38, 52):
        if s[i] in s[:38]:
            repeats.add(s[i])
    for repeat in repeats:
        s = s.replace(repeat, '')
    return s