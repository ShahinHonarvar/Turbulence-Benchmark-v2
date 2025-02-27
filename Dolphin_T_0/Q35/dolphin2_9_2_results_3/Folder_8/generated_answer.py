def remove_repeat_chars(my_string):
    repeat_chars = [my_string[i] for i in range(45, 48) if my_string.count(my_string[i]) > 1]
    for char in repeat_chars:
        my_string = my_string.replace(char, '')
    return my_string