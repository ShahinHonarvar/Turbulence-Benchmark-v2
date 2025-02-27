def insert_before_character(s):
    result = ''
    for i in range(len(s)):
        if s[i] == 'e':
            result += 'E'
        result += s[i]
    return result