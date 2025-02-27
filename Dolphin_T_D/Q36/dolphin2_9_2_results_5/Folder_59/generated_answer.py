def filter_chars(string):
    for char in range(ord('?'), ord('k')):
        new_string = ''
        for i in range(len(string)):
            if i < 3 or i >= 8:
                new_string += string[i]
            elif string[i] != chr(char):
                new_string += string[i]
        string = new_string
    return string