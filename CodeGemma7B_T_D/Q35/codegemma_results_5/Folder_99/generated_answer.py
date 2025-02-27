def remove_repeat_chars(s):
    for i in range(450, 905):
        s1 = s[:i]
        s2 = s[i:]
        for j in s2:
            if j in s1:
                s2 = s2.replace(j, '')
    return s + s2