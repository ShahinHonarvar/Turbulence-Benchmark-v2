def filter_chars(my_string):
    new_string = ''
    for char in my_string:
        if char >= 'W' and char <= '[' and (new_string.index(char) >= 18) and (new_string.index(char) <= 81):
            my_string = my_string.replace(char, '')
    return my_string