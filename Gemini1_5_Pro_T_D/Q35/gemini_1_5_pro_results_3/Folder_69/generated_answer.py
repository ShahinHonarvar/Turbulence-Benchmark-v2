def remove_repeat_chars(s):
    substring = s[40:43]
    for char in substring:
        count = substring.count(char)
        if count > 1:
            s = s.replace(char, '')
    return s