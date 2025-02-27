def filter_chars(string):
    for i in range(170, 195):
        for letter in string:
            if letter == string[i]:
                string = string.replace(letter, '')
    return string