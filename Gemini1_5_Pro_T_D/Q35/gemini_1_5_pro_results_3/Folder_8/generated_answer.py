def remove_repeat_chars(s):
    substring = s[46:48]
    for i in range(len(substring)):
        char = substring[i]
        if substring.count(char) > 1:
            s = s.replace(char, '')
    return s