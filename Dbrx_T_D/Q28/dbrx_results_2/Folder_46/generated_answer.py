def return_nth_smallest_ascii(input_string):
    characters = sorted(input_string[34:86])
    if len(characters) < 20:
        return None
    else:
        return characters[19]