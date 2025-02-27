def remove_repeat_chars(s):
    for i in range(86, 89):
        if s[i] in s[i + 1:]:
            for k in s[i + 1:]:
                if s[i] == k:
                    s = s.replace(k, '')
    return s