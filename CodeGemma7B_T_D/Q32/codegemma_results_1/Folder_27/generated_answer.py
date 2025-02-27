def insert_after_character(mystring):
    for i in range(len(mystring)):
        if mystring[i] == 'N':
            a += mystring[i] + 'j'
        else:
            a += mystring[i]
    return a