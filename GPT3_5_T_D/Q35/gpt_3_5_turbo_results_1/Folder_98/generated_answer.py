def remove_repeat_chars(string):
    for char in string[:7]:
        if string.count(char) > 1:
            string = string.replace(char, '')
    return string