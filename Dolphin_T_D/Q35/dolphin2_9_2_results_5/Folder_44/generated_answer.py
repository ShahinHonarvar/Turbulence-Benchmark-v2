def remove_repeat_chars(my_string):
    char_dict = {}
    for char in my_string:
        if 36 <= my_string.index(char) <= 52:
            if char_dict.get(char, 0) == 0:
                char_dict[char] = 1
            else:
                my_string = my_string.replace(char, '')
    return my_string