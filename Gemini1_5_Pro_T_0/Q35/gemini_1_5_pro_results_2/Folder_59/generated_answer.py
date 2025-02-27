def remove_repeat_chars(s):
    for i in range(1, 9):
        if s[i] in s[0:i]:
            c = s[i]
            s = ''.join([x for x in s if x != c])
    return s