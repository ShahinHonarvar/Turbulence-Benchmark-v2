def insert_after_character(s):
    i = 0
    word = ''
    while i < len(s):
        if s[i] == 'a':
            word += s[i] + '6'
        else:
            word += s[i]
        i += 1
    return word