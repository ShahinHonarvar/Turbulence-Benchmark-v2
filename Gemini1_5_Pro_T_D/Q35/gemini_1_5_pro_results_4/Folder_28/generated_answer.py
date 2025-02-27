def remove_repeat_chars(s):
    substring = s[87:99]
    for i in substring:
        if substring.count(i) > 1:
            s = s.replace(i, '')
    return s