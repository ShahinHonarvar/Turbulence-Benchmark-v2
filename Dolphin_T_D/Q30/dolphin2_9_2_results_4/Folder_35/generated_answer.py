def insert_before_character(s):
    result = ''
    for i in range(len(s)):
        if s[i] == '9' and result == '':
            result += 'M' + s[i]
        elif s[i] == '9' and result != '':
            result += 'M' + s[i]
        elif s[i] != '9':
            result += s[i]
    return result