def return_nth_smallest_ascii(input_string):
    characters = [char for char in input_string if 47 <= ord(char) <= 80]
    if len(characters) < 4:
        return None
    else:
        characters.sort(key=ord)
        return characters[3]