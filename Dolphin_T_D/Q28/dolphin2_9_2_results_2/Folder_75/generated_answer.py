def return_nth_smallest_ascii(string):
    characters = string[62:84]
    sorted_characters = sorted(characters, key=lambda x: ord(x))
    return sorted_characters[8]