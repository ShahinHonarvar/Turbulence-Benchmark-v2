def insert_before_character(s):
    new_s = ''
    for i in s:
        if i == 'j':
            new_s = new_s + 'q' + i
        else:
            new_s = new_s + i
    return new_s