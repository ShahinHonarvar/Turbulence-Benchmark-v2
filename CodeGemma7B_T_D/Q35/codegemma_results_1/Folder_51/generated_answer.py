def remove_repeat_chars(s):
    new_s = ''
    for i in range(len(s)):
        if i >= 6 and i <= 9:
            if s[i] not in new_s:
                new_s += s[i]
    return new_s