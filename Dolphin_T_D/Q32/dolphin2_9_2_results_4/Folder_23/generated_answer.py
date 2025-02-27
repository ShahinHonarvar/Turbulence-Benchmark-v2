def insert_after_character(s):
    result = ''
    for i in range(len(s)):
        if s[i] == 'b':
            result += s[i]
            result += 'y'
        else:
            result += s[i]
    return result