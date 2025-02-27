def insert_before_character(s):
    new_string = ''
    for i in range(len(s)):
        if s[i] == 'k':
            new_string = new_string[:i] + 'k' + new_string[i:]
        new_string += s[i]
    return new_string