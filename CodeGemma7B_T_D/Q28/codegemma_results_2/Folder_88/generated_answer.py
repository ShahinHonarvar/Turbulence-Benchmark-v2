def return_nth_smallest_ascii(string):
    characters = [char for char in string[38:65]]
    characters.sort(key=ord)
    return characters[13]