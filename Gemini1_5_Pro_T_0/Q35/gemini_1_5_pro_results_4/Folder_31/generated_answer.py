def remove_repeat_chars(s):
    substring = s[34:78]
    for char in substring:
        if substring.count(char) > 1:
            s = s.replace(char, '')
    return s