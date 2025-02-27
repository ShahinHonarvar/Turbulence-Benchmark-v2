def remove_repeat_chars(s):
    alter_s = list(s)
    for i in range(51, 76):
        if alter_s[i] in alter_s[51:76]:
            j = alter_s.count(alter_s[i])
            del alter_s[i]
            if j > 1:
                i -= 1
    s = ''.join(alter_s)
    return s