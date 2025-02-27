def insert_after_character(s):
    result = ''
    for i in range(len(s)):
        if s[i] == 'A':
            result += s[i] + 'H'
        else:
            result += s[i]
    return result