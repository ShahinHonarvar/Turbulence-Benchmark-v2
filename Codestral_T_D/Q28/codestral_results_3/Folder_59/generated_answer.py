def return_nth_smallest_ascii(string):
    characters = string[0:12]
    sorted_characters = sorted(characters, key=ord)
    return sorted_characters[11]