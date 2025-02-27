def insert_before_character(s):
    result = ''
    for i in range(len(s)):
        if s[i] == 'c':
            result += 'G'
        result += s[i]
    return result