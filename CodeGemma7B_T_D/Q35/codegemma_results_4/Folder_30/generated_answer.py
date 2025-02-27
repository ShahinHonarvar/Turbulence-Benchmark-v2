def remove_repeat_chars(string):
    for i in range(22, 24):
        char = string[i]
        if string.count(char) > 1:
            for j in range(string.index(char), len(string)):
                if string[j] == char:
                    string = string[:j] + string[j + 1:]
    return string