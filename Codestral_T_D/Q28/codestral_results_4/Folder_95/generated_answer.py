def return_nth_smallest_ascii(string):
    characters = string[1:47]
    sorted_chars = sorted(characters, key=ord)
    return sorted_chars[12]