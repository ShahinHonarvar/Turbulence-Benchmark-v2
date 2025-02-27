def return_nth_smallest_ascii(input_string):
    characters = sorted(input_string[:5])
    return characters[3] if len(characters) > 3 else None