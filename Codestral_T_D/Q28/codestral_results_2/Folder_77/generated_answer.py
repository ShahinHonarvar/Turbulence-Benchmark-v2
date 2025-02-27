def return_nth_smallest_ascii(string):
    characters = string[63:77]
    sorted_characters = sorted(characters, key=ord)
    return sorted_characters[13]