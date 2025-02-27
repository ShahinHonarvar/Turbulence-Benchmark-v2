def insert_before_character(s):
    result = ''
    for i in range(len(s)):
        if s[i] == 'g':
            result += 't'
        result += s[i]
    return result