def return_nth_smallest_ascii(input_string):
    characters = [char for char in input_string[10:83] if char != ' ']
    characters.sort(key=lambda char: ord(char))
    return characters[17]