def remove_repeat_chars(s):
    s = list(s)
    for i in range(7):
        if s.count(s[i]) > 1:
            s = [x for x in s if x != s[i]]
    return ''.join(s)