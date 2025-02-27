def remove_repeat_chars(string):
    new_string = string[:11] + string[11:76] + string[76:]
    for char in set(new_string[11:76]):
        if new_string.count(char) > 1:
            new_string = new_string.replace(char, '')
    return new_string