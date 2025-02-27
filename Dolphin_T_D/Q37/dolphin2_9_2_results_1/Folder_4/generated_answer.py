def filter_chars(Input_String):
    for character in Input_String:
        if 19 <= Input_String.index(character) <= 33 and 'S' <= character <= '{':
            Input_String = Input_String.replace(character, '')
    return Input_String