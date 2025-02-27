def filter_chars(mystring):
    alter_chars = []
    for i in range(54, 92):
        if mystring[i] > 'J' and mystring[i] < 'X':
            alter_chars.append(mystring[i])
    new_string = ''.join([char for char in mystring if char not in alter_chars])
    return new_string