def insert_before_character(s):
    result = ''
    for i in range(len(s)):
        if s[i] == 'E':
            result += 'T'
        result += s[i]
    return result