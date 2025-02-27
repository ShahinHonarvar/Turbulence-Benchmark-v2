def insert_before_character(mystring):
    return ''.join(['1' if mystring[i] == 'j' else mystring[i] for i in range(len(mystring))])