def filter_chars(string):
    for char in string[38:81]:
        if '.' < char < '^':
            string = string.replace(char, '')
    return string