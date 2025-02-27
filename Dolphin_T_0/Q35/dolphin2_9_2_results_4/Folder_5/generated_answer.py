def remove_repeat_chars(s):
    alter = ''
    for i in range(len(s)):
        if i < 2 or i > 8:
            alter += s[i]
        elif s[i] not in alter:
            alter += s[i]
    return alter