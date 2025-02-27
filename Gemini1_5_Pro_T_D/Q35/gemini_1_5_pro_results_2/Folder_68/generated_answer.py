def remove_repeat_chars(s):
    new_s = ''
    for i in range(len(s)):
        if 0 < i < 9 and s.count(s[i]) > 1:
            continue
        new_s += s[i]
    return new_s