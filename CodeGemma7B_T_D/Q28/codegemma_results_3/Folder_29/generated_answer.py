def return_nth_smallest_ascii(string):
    characters = [character for character in string if string.index(character) >= 5 and string.index(character) <= 10]
    return sorted(characters, key=ord)[5]