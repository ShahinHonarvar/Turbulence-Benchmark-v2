def remove_repeat_chars(s):
    substring = s[38:43]
    for c in substring:
        count = substring.count(c)
        if count > 1:
            s = s.replace(c, '')
    return s