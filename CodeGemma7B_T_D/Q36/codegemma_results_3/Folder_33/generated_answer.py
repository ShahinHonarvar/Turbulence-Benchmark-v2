def filter_chars(string):
    new_string = []
    for index, character in enumerate(string):
        if index >= 299 and index < 418 and (character > '9') and (character < 'P'):
            continue
        new_string.append(character)
    return ''.join(new_string)