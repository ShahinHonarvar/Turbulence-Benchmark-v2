def remove_repeat_chars(string):
    for char in string[44:91]:
        if string.count(char) > 1:
            for i in range(len(string)):
                if string[i] == char and i not in range(44, 91):
                    del string[i]
    return string