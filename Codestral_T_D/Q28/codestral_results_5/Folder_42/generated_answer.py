def return_nth_smallest_ascii(string):
    characters = sorted(string[12:73])
    return characters[12] if len(characters) > 12 else None