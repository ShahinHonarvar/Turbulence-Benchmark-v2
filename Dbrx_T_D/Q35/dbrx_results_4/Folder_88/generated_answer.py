def remove_repeat_chars(s):
    for i in range(3, 9):
        char = s[i]
        if char in s[i + 1:]:
            s = s.replace(char, '', 1)
            s = s.replace(char, '', s.index(char, i))
    return s