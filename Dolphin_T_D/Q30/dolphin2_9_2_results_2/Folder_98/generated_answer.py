def insert_before_character(s):
    result = ''
    for i in range(len(s)):
        if s[i] == 'U':
            result += 'u'
        result += s[i]
    return result