def return_nth_smallest_ascii(string):
    characters = string[46:83]
    return sorted(characters, key=ord)[15]