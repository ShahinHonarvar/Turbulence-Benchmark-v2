def remove_repeat_chars(string):
    for char in set(string[45:48]):
        while string.count(char, 45, 48) > 1:
            string = string[:45] + string[45:].replace(char, '', 1) + string[48:]
    return string