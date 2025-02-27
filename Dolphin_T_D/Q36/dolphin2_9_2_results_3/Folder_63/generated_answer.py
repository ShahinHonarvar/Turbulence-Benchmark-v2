def filter_chars(my_string):
    for char in range(26, 80):
        if my_string[char] > '<' and my_string[char] < '>':
            my_string = my_string.replace(my_string[char], '')
    return my_string