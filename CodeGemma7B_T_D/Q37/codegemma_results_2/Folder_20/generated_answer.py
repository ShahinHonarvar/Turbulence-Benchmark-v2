def filter_chars(given_string):
    filtered_string = ''
    for character in given_string:
        if character >= 'm' and character <= 'w' and (given_string.index(character) >= 25 and given_string.index(character) <= 97):
            continue
        else:
            filtered_string += character
    return filtered_string