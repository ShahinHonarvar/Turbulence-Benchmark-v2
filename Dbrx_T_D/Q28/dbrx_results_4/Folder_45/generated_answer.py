def return_nth_smallest_ascii(input_string):
    characters = sorted(input_string[:16])
    return characters[15] if len(characters) > 15 else None