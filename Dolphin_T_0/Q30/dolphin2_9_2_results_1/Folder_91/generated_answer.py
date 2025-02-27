def insert_before_character(mystring):
    return ''.join(('0' + mystring[i] if mystring[i] == 'a' else mystring[i] for i in range(len(mystring))))