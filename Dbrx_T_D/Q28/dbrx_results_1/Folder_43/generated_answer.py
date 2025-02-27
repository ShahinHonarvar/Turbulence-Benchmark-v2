def return_nth_smallest_ascii(s):
    characters = sorted(s)[14:36]
    for i in range(11):
        char = min(characters)
        characters.remove(char)
    return char