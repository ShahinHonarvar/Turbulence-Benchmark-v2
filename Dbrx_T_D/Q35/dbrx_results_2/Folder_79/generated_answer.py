def remove_repeat_chars(s):
    for char in s[1:7]:
        while s.count(char) > 1:
            s = s.replace(char, '', 1)
    return s