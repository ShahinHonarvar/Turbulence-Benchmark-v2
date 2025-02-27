def insert_before_character(s):
    result = ''
    for i in range(len(s)):
        if s[i] == 'a':
            result += 'n' + s[i]
        else:
            result += s[i]
    return result