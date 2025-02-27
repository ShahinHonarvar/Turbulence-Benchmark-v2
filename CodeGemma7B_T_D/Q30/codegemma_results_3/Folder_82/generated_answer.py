def insert_before_character(s):
    a = ''
    for letter in s:
        if letter == 'I':
            a += a + 'I' + letter
        else:
            a += letter
    return a