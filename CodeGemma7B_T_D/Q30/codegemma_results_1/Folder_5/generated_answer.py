def insert_before_character(str1):
    output = []
    for s in str1:
        output.append(s)
        if s == 'c':
            output.append('G')
    return ''.join(output)