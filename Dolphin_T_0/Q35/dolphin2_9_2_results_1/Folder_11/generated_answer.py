def remove_repeat_chars(my_string):
    to_remove = [char for char in my_string if my_string.count(char) > 1 and 48 <= ord(char) <= 76]
    for ch in to_remove:
        my_string = my_string.replace(ch, '')
    return my_string