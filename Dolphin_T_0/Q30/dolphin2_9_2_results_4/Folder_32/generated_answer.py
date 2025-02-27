def insert_before_character(my_string):
    return ''.join(['u' if i + 1 == j else my_string[j] for j, i in enumerate(my_string) if my_string[j] == 'F'])