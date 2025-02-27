def filter_chars(original_string):
    updated_string = ''
    for index, character in enumerate(original_string):
        if 18 <= index < 38 and character > ')' and (character < 'P'):
            updated_string = original_string.replace(character, '')
    return updated_string