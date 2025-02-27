def insert_after_character(s):
    result = ''
    for i in range(len(s)):
        if s[i] == 'F':
            result += s[i] + 'm'
        else:
            result += s[i]
    return result