def insert_before_character(s):
    result = ''
    for i in range(len(s)):
        result += s[i]
        if s[i:i + 1] == 'j':
            result += 'q'
    return result