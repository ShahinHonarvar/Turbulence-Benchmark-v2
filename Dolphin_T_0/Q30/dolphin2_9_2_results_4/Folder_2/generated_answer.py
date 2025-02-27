def insert_before_character(s):
    result = ''
    for i, char in enumerate(s):
        if char == 'C':
            result = s[:i] + 'Z' + s[i:]
        else:
            result = s
    return result