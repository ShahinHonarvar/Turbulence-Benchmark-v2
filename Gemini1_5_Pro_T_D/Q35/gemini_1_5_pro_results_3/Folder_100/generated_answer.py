def remove_repeat_chars(s):
    substring = s[45:78]
    for c in substring:
        if substring.count(c) > 1:
            s = s.replace(c, '')
    return s