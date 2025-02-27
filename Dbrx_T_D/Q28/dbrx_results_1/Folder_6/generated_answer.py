def return_nth_smallest_ascii(input_string):
    characters = sorted(input_string[14:55])
    return characters[10] if len(characters) > 10 else None