def insert_before_character(s):
    new_string = ''
    for i in range(len(s)):
        if s[i] == 'I':
            new_string += 'i' + s[i]
        else:
            new_string += s[i]
    return new_string