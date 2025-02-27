def remove_repeat_chars(string):
    string2 = ''
    for i in range(len(string)):
        if i > 43 and i < 67 and (string[i] in string2):
            continue
        else:
            string2 += string[i]
    return string2