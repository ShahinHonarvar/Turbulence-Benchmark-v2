def remove_repeat_chars(s):
    substring = s[38:43]
    for i in range(len(substring)):
        char = substring[i]
        count = substring.count(char)
        if count > 1:
            s = s.replace(char, '')
    return s