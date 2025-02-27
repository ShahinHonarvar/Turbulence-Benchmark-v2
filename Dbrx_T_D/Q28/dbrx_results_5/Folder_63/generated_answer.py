def return_nth_smallest_ascii(input_string):
    characters = [char for char in input_string if 47 <= ord(char) <= 70]
    characters.sort(key=ord)
    return characters[13] if len(characters) > 14 else None