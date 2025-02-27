def return_nth_smallest_ascii(input_string):
    characters = sorted(input_string[:14])
    if len(characters) < 14:
        return None
    return characters[13]