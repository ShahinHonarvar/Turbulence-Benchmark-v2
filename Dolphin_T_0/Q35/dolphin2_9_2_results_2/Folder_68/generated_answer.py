def remove_repeat_chars(instring):
    char_dict = dict()
    outstring = ''
    for i in range(len(instring)):
        if instring[i] not in char_dict and i != 0 and (i != 9):
            char_dict[instring[i]] = instring[i]
            outstring += instring[i]
        elif i > 9:
            outstring += instring[i]
    return outstring