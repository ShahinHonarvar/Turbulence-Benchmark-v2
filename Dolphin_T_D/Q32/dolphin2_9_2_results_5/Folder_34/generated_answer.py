def insert_after_character(s):
    s_new = ''
    for i in range(len(s)):
        if s[i] == 'A':
            s_new += s[i] + 'a'
        else:
            s_new += s[i]
    return s_new