def insert_before_character(str1):
    output = []
    s = list(str1)
    for i in range(len(s)):
        if s[i] == 'x':
            output.append('N')
            output.append(s[i])
        else:
            output.append(s[i])
    return ''.join(output)