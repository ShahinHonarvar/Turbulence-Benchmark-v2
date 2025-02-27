def filter_chars(my_string):
    l = len(my_string)
    for i in range(l):
        if 39 < i < 87 and my_string[i] > '!' and (my_string[i] < '}'):
            while my_string[i] in my_string:
                my_string = my_string[:i] + my_string[i + 1:]
            break
    return my_string