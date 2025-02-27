def filter_chars(my_string):
    for char in my_string[27:75]:
        if 'A' < char < 'i':
            my_string = my_string.replace(char, '')
    return my_string