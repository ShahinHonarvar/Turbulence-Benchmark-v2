def remove_repeat_chars(s):
    substring = s[201:202]
    for char in substring:
        count = substring.count(char)
        if count > 1:
            s = s.replace(char, '')
    return s