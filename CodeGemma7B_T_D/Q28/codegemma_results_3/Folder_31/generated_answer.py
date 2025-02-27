def return_nth_smallest_ascii(string):
    characters = sorted([char for char in string[10:83] if char.ascii_lowercase])
    return characters[17]