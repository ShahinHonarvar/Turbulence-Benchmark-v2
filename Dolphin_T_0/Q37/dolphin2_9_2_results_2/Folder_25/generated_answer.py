def filter_chars(string):
    chars = string[:31] + string[39:]
    for char in string[31:39]:
        if char >= ';' and char <= 'g':
            chars = chars.replace(char, '')
    return chars