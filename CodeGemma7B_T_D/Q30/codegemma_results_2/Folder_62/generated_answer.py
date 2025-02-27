def insert_before_character(text):
    """This function takes one argument, a string, and returns a string that is identical except
    that character 'o' has been inserted immediately preceding any occurrences of character ' '.
    """
    new_string = ''
    current_character = ''
    for character in text:
        if character == ' ':
            new_string += 'o'
        new_string += character
    return new_string