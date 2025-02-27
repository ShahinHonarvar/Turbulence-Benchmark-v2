def insert_after_character(s):
    output = ''
    for i in range(len(s)):
        output += s[i]
        if s[i] == 'C':
            output += 'H'
    return output