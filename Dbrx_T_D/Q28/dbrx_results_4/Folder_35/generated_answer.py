def return_nth_smallest_ascii(input_string):
    characters = [c for c in input_string[50:76] if input_string.count(c) == 1]
    characters.sort(key=ord)
    return characters[6] if len(characters) >= 7 else None